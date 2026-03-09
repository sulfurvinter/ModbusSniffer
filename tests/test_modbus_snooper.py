from unittest.mock import MagicMock, patch
from modbus_sniffer.serial_snooper import SerialSnooper


@patch("modbus_sniffer.serial_snooper.serial.Serial")
def test_serial_snooper_read_and_process(mock_serial):
    serial_instance = MagicMock()
    serial_instance.read.return_value = (
        b"\x01\x03\x02\x00\x0a\x79\x84"  # example modbus frame
    )
    mock_serial.return_value = serial_instance

    logger = MagicMock()

    snooper = SerialSnooper(
        main_logger=logger,
        port="/dev/null",
        baud=9600,
        parity="E",
        timeout=1,
        raw_log=False,
        raw_only=False,
        csv_log=False,
        daily_file=False,
    )

    with snooper:
        data = snooper.read_raw()
        assert data == b"\x01\x03\x02\x00\x0a\x79\x84"
        snooper.process_data(data)

    logger.info.assert_called()  # at least one logging call


def test_raw_only_logging(monkeypatch):
    logger = MagicMock()
    with patch("modbus_sniffer.serial_snooper.serial.Serial"):
        snooper = SerialSnooper(
            main_logger=logger,
            port="/dev/null",
            baud=9600,
            parity="E",
            timeout=1,
            raw_log=False,
            raw_only=True,
            csv_log=False,
            daily_file=False,
        )
        # supplying some bytes should log and return early
        snooper.process_data(b"\x01\x02")
        assert logger.info.called


def test_process_data_accumulates_and_decodes(monkeypatch):
    logger = MagicMock()
    with patch("modbus_sniffer.serial_snooper.serial.Serial"):
        snooper = SerialSnooper(
            main_logger=logger,
            port="/dev/null",
            baud=9600,
            parity="E",
            timeout=1,
            raw_log=False,
            raw_only=False,
            csv_log=False,
            daily_file=False,
        )
        # patch ModbusParser to record calls
        called = {}
        class FakeParser:
            def __init__(self, log, csv, raw_log, trashdata, on_parsed=None):
                called['init'] = True
            def decodeModbus(self, data):
                called['decode'] = True
                return b''
        monkeypatch.setattr('modbus_sniffer.serial_snooper.ModbusParser', FakeParser)
        snooper.data = bytearray(b"123")
        snooper.process_data(b"")  # triggers check for len(self.data)>2
        assert called.get('decode')


def test_emit_parsed_data_calls_handler():
    logger = MagicMock()
    with patch("modbus_sniffer.serial_snooper.serial.Serial"):
        received = []
        def handler(data):
            received.append(data)
        snooper = SerialSnooper(
            main_logger=logger,
            port="/dev/null",
            baud=9600,
            parity="E",
            timeout=1,
            raw_log=False,
            raw_only=False,
            csv_log=False,
            daily_file=False,
            data_handler=handler,
        )
        snooper.emit_parsed_data({'foo':'bar'})
        assert received == [{'foo':'bar'}]


def test_open_and_close_calls_connection_and_csv(monkeypatch):
    logger = MagicMock()
    mock_conn = MagicMock()
    with patch('modbus_sniffer.serial_snooper.serial.Serial', return_value=mock_conn):
        snooper = SerialSnooper(
            main_logger=logger,
            port="/dev/null",
            baud=9600,
            parity="E",
            timeout=1,
            raw_log=False,
            raw_only=False,
            csv_log=True,
            daily_file=False,
        )
        # __enter__ did not open connection (constructor did), test open/close
        snooper.open()
        mock_conn.open.assert_called_once()
        snooper.close()
        mock_conn.close.assert_called_once()
        # csv_logger closed as well (should not raise)

