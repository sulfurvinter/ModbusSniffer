import os
import csv
import tempfile
from unittest import mock
from itertools import cycle
from modbus_sniffer.csv_logger import CSVLogger


def test_no_csv_logging():
    logger = CSVLogger(enable_csv=False)
    logger.log_data("2024-01-01 00:00:00", 1, "READ", 0, 2, [123, 456])
    assert logger.csv_file is None
    logger.close()  # should not raise


def test_initial_csv_file_creation():
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        assert logger.csv_file is not None
        assert os.path.exists(logger.csv_file.name)
        with open(logger.csv_file.name) as f:
            header = f.readline().strip()
            assert header.startswith("Timestamp,Slave ID,Operation")
        logger.close()


def test_expand_header_and_logging():
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        logger.log_data("2024-01-01 12:00:00", 1, "READ", 100, 2, [111, 222])
        file_path = logger.csv_file.name  # <- ZAPISZ PRZED close
        logger.close()

        with open(file_path, newline="") as f:
            rows = list(csv.reader(f))
            assert rows[0] == [
                "Timestamp",
                "Slave ID",
                "Operation",
                "Reg_1_100",
                "Reg_1_101",
            ]
            assert rows[1][:3] == ["2024-01-01 12:00:00", "1", "READ"]
            assert "111" in rows[1]
            assert "222" in rows[1]


def test_header_rewrite_on_new_register():
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        logger.log_data("2024-01-01 12:00:00", 1, "READ", 100, 1, [42])
        old_file = logger.csv_file.name
        logger.log_data("2024-01-01 12:01:00", 1, "READ", 101, 1, [84])
        logger.close()

        with open(old_file, newline="") as f:
            rows = list(csv.reader(f))
            assert "Reg_1_100" in rows[0]
            assert "Reg_1_101" in rows[0]
            assert rows[1][rows[0].index("Reg_1_100")] == "42"
            assert rows[2][rows[0].index("Reg_1_101")] == "84"


@mock.patch("modbus_sniffer.csv_logger.CSVLogger._get_datetime_str")
@mock.patch("modbus_sniffer.csv_logger.CSVLogger._get_date_str")
def test_daily_rotation(mock_date_str, mock_datetime_str):
    # mockowanie dat: 2x ten sam dzień, potem nowy dzień
    mock_date_str.side_effect = cycle(["20240101", "20240101", "20240102"])
    # mockowanie daty i czasu dla nazwy pliku
    mock_datetime_str.side_effect = ["2024-01-01_12-00-00", "2024-01-02_08-00-00"]

    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, daily_file=True, output_dir=tmpdir)
        first_file = logger.csv_file.name

        logger.log_data("2024-01-01 12:00:00", 1, "READ", 100, 1, [42])
        logger.log_data("2024-01-02 08:00:00", 1, "READ", 100, 1, [43])
        second_file = logger.csv_file.name

        assert os.path.exists(first_file)
        assert os.path.exists(second_file)
        assert first_file != second_file
        logger.close()


def test_close_twice_is_safe():
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        logger.close()
        logger.close()  # should not raise


def test_get_date_and_datetime_str():
    # ensure utility methods return formatted strings
    logger = CSVLogger(enable_csv=False)
    ds = logger._get_date_str()
    assert len(ds) == 8 and ds.isdigit()
    dt = logger._get_datetime_str()
    assert len(dt) >= 19 and dt[4] == "-"


def test_rewrite_file_with_no_csv_file():
    # if csv_file is None early return
    logger = CSVLogger(enable_csv=False)
    # should simply return without error
    logger._rewrite_file_with_new_header()


def test_expand_header_no_change():
    # when requested registers already in map, header should not rewrite
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        # first log to create entries
        logger.log_data("t", 1, "READ", 10, 1, [1])
        old_cols = list(logger.columns)
        logger.log_data("t2", 1, "READ", 10, 1, [2])
        # columns unchanged
        assert logger.columns == old_cols
        logger.close()


def test_rewrite_file_handles_short_old_rows():
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = CSVLogger(enable_csv=True, output_dir=tmpdir)
        path = logger.csv_file.name
        # manually write header with two columns and a row with only one value
        logger.csv_file.close()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Slave ID", "Operation"])
            writer.writerow(["2024","1"])
        # instruct logger to rewrite with additional column
        logger.columns.append("Extra")
        logger._rewrite_file_with_new_header()
        logger.csv_file.close()
        with open(path, newline="") as f:
            rows = list(csv.reader(f))
            assert rows[0][-1] == "Extra"
            # second row should have empty slot for the new column
            assert len(rows[1]) == 4 and rows[1][-1] == ""

