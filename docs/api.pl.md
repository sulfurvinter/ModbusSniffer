# Dokumentacja API

Ta sekcja zawiera przegląd głównych klas i funkcji w ModbusSniffer.

## Główne Klasy

### ModbusParser

Parsuje surowe dane Modbus RTU na ustrukturyzowane ramki.

**Metody:**
- `parse_frame(data: bytes) -> dict`: Dekoduje pojedynczą ramkę.
- `validate_crc(data: bytes) -> bool`: Sprawdza poprawność CRC.

**Przykład:**
```python
from modbus_sniffer.modbus_parser_new import ModbusParser

parser = ModbusParser()
frame = parser.parse_frame(b'\x01\x03\x00\x00\x00\x01\x84\x0A')
print(frame)  # {'address': 1, 'function': 3, 'data': ...}
```

### SerialSnooper

Obsługuje komunikację przez port szeregowy.

**Metody:**
- `open_port(port: str, baud: int) -> None`: Otwiera port szeregowy.
- `read_data() -> bytes`: Odczytuje przychodzące dane.

**Przykład:**
```python
from modbus_sniffer.serial_snooper import SerialSnooper

snooper = SerialSnooper()
snooper.open_port('/dev/ttyUSB0', 9600)
data = snooper.read_data()
```

### MainLogger

Koordynuje logowanie i aktualizacje GUI.

**Metody:**
- `start_sniffing() -> None`: Rozpoczyna przechwytywanie.
- `stop_sniffing() -> None`: Kończy przechwytywanie.

## Narzędzia

### SnifferUtils

Funkcje pomocnicze do przetwarzania danych.

**Funkcje:**
- `format_hex(data: bytes) -> str`: Formatuje bajty jako hex string.
- `calculate_crc(data: bytes) -> int`: Oblicza CRC Modbus.

**Przykład:**
```python
from modbus_sniffer.sniffer_utils import format_hex

hex_str = format_hex(b'\x01\x02\x03')
print(hex_str)  # '01 02 03'
```