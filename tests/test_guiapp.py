import pytest
from unittest.mock import MagicMock
from modbus_sniffer.gui import GUIApp, AutoResizeTable, AdvancedAlignDelegate
from PyQt6.QtCore import Qt


@pytest.fixture
def app_instance(qtbot):
    app = GUIApp()
    qtbot.addWidget(app)
    return app


def test_default_state(app_instance):
    assert app_instance.start_btn.isEnabled()
    assert not app_instance.stop_btn.isEnabled()
    assert app_instance.port_input.currentText() == ""


def test_log_window_updates(app_instance, qtbot):
    test_log = "Master: Sending request"
    qtbot.wait(100)
    app_instance.update_log_window(test_log)

    assert "Master" in app_instance.log_window.toPlainText()


def test_add_parsed_data_new_entry(app_instance):
    example_frame = {
        "timestamp": "2024-01-01T12:00:00",
        "function": 3,
        "function_name": "Read Holding Registers",
        "message_type": "response",
        "slave_id": 1,
        "data_address": 100,
        "data_qty": 2,
        "byte_cnt": 4,
        "data": [4660, 22136],
        "exception_code": None,
        "read_address": None,
        "read_quantity": None,
        "write_address": None,
        "write_quantity": None,
    }

    app_instance.add_parsed_data(example_frame)
    assert len(app_instance.data_dict) == 1
    assert app_instance.table.rowCount() == 1


def test_refresh_serial_ports(monkeypatch, app_instance):
    # simulate two ports returned, including a windows style path
    class FakePort:
        def __init__(self, loc):
            self._loc = loc
        def systemLocation(self):
            return self._loc
    monkeypatch.setattr(
        "modbus_sniffer.gui.QSerialPortInfo.availablePorts",
        lambda: [FakePort("/dev/tty1"), FakePort("\\\\.\\COM3")],
    )
    import platform
    monkeypatch.setattr(platform, "system", lambda: "Windows")
    # call showPopup which triggers refresh
    app_instance.port_input.showPopup()
    # should contain cleaned names
    assert "COM3" in [app_instance.port_input.itemText(i) for i in range(app_instance.port_input.count())]


def test_refresh_serial_ports_non_windows(monkeypatch, app_instance):
    class FakePort:
        def __init__(self, loc):
            self._loc = loc
        def systemLocation(self):
            return self._loc
    monkeypatch.setattr(
        "modbus_sniffer.gui.QSerialPortInfo.availablePorts",
        lambda: [FakePort("/dev/tty2")],
    )
    import platform
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    app_instance.port_input.showPopup()
    assert "/dev/tty2" in [app_instance.port_input.itemText(i) for i in range(app_instance.port_input.count())]


def test_update_log_window_coloring(app_instance):
    # master messages alternate colors and set last_master
    app_instance.last_master = None
    app_instance.last_ok_color = "blue"
    app_instance.update_log_window("Master test")
    assert "color" in app_instance.log_window.toHtml()
    # second master should toggle color
    app_instance.update_log_window("Master again")
    assert app_instance.last_ok_color in ("blue", "green")
    # slave message triggers separation and color
    app_instance.update_log_window("Slave responded")
    assert "Slave" in app_instance.log_window.toPlainText()


def test_update_parsed_data_various_types(app_instance):
    # list input
    app_instance.data_dict = {}
    frame1 = {"slave_id":1,"function":3,"data_qty":1,"data_address":0,"message_type":"req","exception_code":None,"timestamp":"t","function_name":"Read Holding Registers","byte_cnt":"","data":[]}
    frame2 = {"slave_id":2,"function":6,"data_qty":1,"data_address":0,"message_type":"req","exception_code":None,"timestamp":"t","function_name":"Write Single Register","byte_cnt":"","data":[]}
    app_instance.update_parsed_data([frame1, frame2])
    assert len(app_instance.data_dict) == 2
    # unknown type
    app_instance.log_window.clear()
    app_instance.update_parsed_data("not a dict")
    assert "Unexpected data type" in app_instance.log_window.toPlainText()


def test_format_table_and_data_fields(app_instance):
    # fc 23 request with numeric values
    val = {
        "function": 23,
        "message_type": "request",
        "read_address": "10",
        "write_address": "20",
        "read_quantity": "2",
        "write_quantity": "3",
        "data_address": "",
        "data_qty": "",
    }
    addr, qty = app_instance.format_table_fields(val)
    assert "R:" in addr and "W:" in addr
    assert "R:" in qty and "W:" in qty
    # invalid numbers cause fallback
    val["read_address"] = "bad"
    addr2, qty2 = app_instance.format_table_fields(val)
    assert "bad" in addr2
    # other function codes
    val2 = {"function": 1, "message_type": "request", "data_address": "5", "data_qty": 10}
    addr3, qty3 = app_instance.format_table_fields(val2)
    assert addr3.startswith("0x") and qty3 == "10"
    # blank address returns empty string
    val3 = {"function": 1, "message_type": "request", "data_address": "", "data_qty": ""}
    addr4, qty4 = app_instance.format_table_fields(val3)
    assert addr4 == "" and qty4 == ""

    # format_data_field exception cases
    o = app_instance.format_data_field({"function_name":"exception","exception_code":5})
    assert "0x05" in o
    o2 = app_instance.format_data_field({"function_name":"exception","exception_code":"X"})
    assert "X" in o2
    o_none = app_instance.format_data_field({"function_name":"exception","exception_code":None})
    assert "Unknown" in o_none
    o3 = app_instance.format_data_field({"function_name":"not","data":[1,2]})
    assert "0x0001" in o3


def test_add_parsed_data_duplicate(app_instance):
    frame = {"slave_id":1,"function":1,"data_qty":1,"data_address":1,"message_type":"req","exception_code":None,
             "timestamp":"t","function_name":"fn","byte_cnt":"","data":[]}
    app_instance.add_parsed_data(frame)
    app_instance.add_parsed_data(frame)
    key = (1,1,1,1,"req",None)
    assert app_instance.data_dict[key]["occurrences"] == 2


def test_clear_and_stop_start_buttons(app_instance, monkeypatch):
    # test clear
    app_instance.data_dict["x"] = 1
    app_instance.log_window.append("log")
    app_instance.last_master = "foo"
    app_instance.last_ok_color = "red"
    app_instance.clear_sniffer_view()
    assert app_instance.table.rowCount() == 0
    assert app_instance.data_dict == {}
    assert app_instance.log_window.toPlainText() == ""
    assert app_instance.last_master is None
    assert app_instance.last_ok_color == "blue"
    # test stop_sniffer
    dummy = MagicMock()
    app_instance.sniffer_thread = dummy
    app_instance.start_btn.setEnabled(False)
    app_instance.stop_btn.setEnabled(True)
    app_instance.stop_sniffer()
    assert app_instance.start_btn.isEnabled()
    assert not app_instance.stop_btn.isEnabled()
    assert "Sniffer stopped" in app_instance.log_window.toPlainText()


def test_start_sniffer_creates_thread(monkeypatch, app_instance):
    # patch normalize and SnifferWorker
    monkeypatch.setattr("modbus_sniffer.gui.normalize_sniffer_config", lambda **kw: {**kw, 'timeout': 1.0})
    class DummyThread:
        def __init__(self, **kw):
            self.kw = kw
            self.log_signal = MagicMock()
            self.parsed_data_signal = MagicMock()
        def start(self):
            self.started = True
    monkeypatch.setattr("modbus_sniffer.gui.SnifferWorker", DummyThread)
    app_instance.port_input.addItem("COM1")
    app_instance.baudrate_input.setCurrentText("9600")
    app_instance.parity_input.setCurrentText("even")
    app_instance.timeout_input.setText("100")
    app_instance.start_sniffer()
    assert isinstance(app_instance.sniffer_thread, DummyThread)
    assert not app_instance.start_btn.isEnabled()
    assert app_instance.stop_btn.isEnabled()


def test_auto_resize_and_delegate():
    table = AutoResizeTable()
    table.resize_columns()
    delegate = AdvancedAlignDelegate()
    delegate.set_column_alignment(0, Qt.AlignmentFlag.AlignLeft)
    # we can't easily create a real index, but we can at least call initStyleOption without error
    from PyQt6.QtWidgets import QStyleOptionViewItem
    from PyQt6.QtCore import QModelIndex
    option = QStyleOptionViewItem()
    index = QModelIndex()
    delegate.initStyleOption(option, index)

