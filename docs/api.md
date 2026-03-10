# API Reference

This section provides an overview of the main classes and functions in ModbusSniffer.

## Core Classes

### ModbusParser

Parses raw Modbus RTU data into structured frames.

**Methods:**
- `parse_frame(data: bytes) -> dict`: Decodes a single frame.
- `validate_crc(data: bytes) -> bool`: Checks CRC validity.

**Example:**
```python
from modbus_sniffer.modbus_parser_new import ModbusParser

parser = ModbusParser()
frame = parser.parse_frame(b'\x01\x03\x00\x00\x00\x01\x84\x0A')
print(frame)  # {'address': 1, 'function': 3, 'data': ...}
```

### SerialSnooper

Handles serial port communication.

**Methods:**
- `open_port(port: str, baud: int) -> None`: Opens serial port.
- `read_data() -> bytes`: Reads incoming data.

**Example:**
```python
from modbus_sniffer.serial_snooper import SerialSnooper

snooper = SerialSnooper()
snooper.open_port('/dev/ttyUSB0', 9600)
data = snooper.read_data()
```

### MainLogger

Coordinates logging and GUI updates.

**Methods:**
- `start_sniffing() -> None`: Begins capture.
- `stop_sniffing() -> None`: Ends capture.

## Utilities

### SnifferUtils

Helper functions for data processing.

**Functions:**
- `format_hex(data: bytes) -> str`: Formats bytes as hex string.
- `calculate_crc(data: bytes) -> int`: Computes Modbus CRC.

**Example:**
```python
from modbus_sniffer.sniffer_utils import format_hex

hex_str = format_hex(b'\x01\x02\x03')
print(hex_str)  # '01 02 03'
```