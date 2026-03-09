import pytest
from unittest.mock import MagicMock, patch
from modbus_sniffer.gui import SnifferWorker


@patch("modbus_sniffer.gui.configure_logging")
@patch("modbus_sniffer.gui.SerialSnooper")
def test_sniffer_worker_run(mock_snooper_class, mock_configure_logging, qtbot):
    fake_logger = MagicMock()
    mock_configure_logging.return_value = fake_logger

    mock_sniffer = MagicMock()
    mock_snooper_class.return_value.__enter__.return_value = mock_sniffer
    mock_sniffer.read_raw.side_effect = [b"data", b"data2", Exception("End")]

    worker = SnifferWorker(
        port="COM1",
        baudrate=9600,
        parity="none",
        timeout=1000,
        csv_log=False,
        raw_log=False,
        raw_only=False,
        daily_file=False,
        log_to_file=False,
    )
    worker.running = True

    # zastępujemy handler, aby nie emitować sygnałów
    worker.handle_parsed_data = MagicMock()

    worker.run()

    assert mock_sniffer.read_raw.call_count == 3
    fake_logger.error.assert_called_once()


def test_emit_log_and_handle_parsed_data():
    worker = SnifferWorker(
        port="COM1",
        baudrate=9600,
        parity="none",
        timeout=1000,
        csv_log=False,
        raw_log=False,
        raw_only=False,
        daily_file=False,
        log_to_file=False,
    )
    logs = []
    datas = []
    worker.log_signal.connect(lambda m: logs.append(m))
    worker.parsed_data_signal.connect(lambda d: datas.append(d))
    worker.emit_log("hello")
    worker.handle_parsed_data({'a':1})
    assert logs == ["hello"]
    assert datas == [{'a':1}]


def test_stop_sets_running_and_calls():
    worker = SnifferWorker(
        port="COM1",
        baudrate=9600,
        parity="none",
        timeout=1000,
        csv_log=False,
        raw_log=False,
        raw_only=False,
        daily_file=False,
        log_to_file=False,
    )
    # patch quit and wait to mark called
    worker.quit = MagicMock()
    worker.wait = MagicMock()
    worker.running = True
    worker.stop()
    assert worker.running is False
    worker.quit.assert_called_once()
    worker.wait.assert_called_once()

