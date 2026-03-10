
# 🐍 ModbusSniffer – Free Modbus RTU Analyzer with GUI (Python / PyQt6)

A lightweight and user-friendly Modbus RTU sniffer tool with a graphical interface.  
Easily analyze and debug communication between PLCs, HMIs, and other Modbus RTU devices via serial ports.

[![GitHub release](https://img.shields.io/github/v/release/niwciu/ModbusSniffer)](https://github.com/niwciu/ModbusSniffer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
  <img src="https://niwciu.github.io/ModbusSniffer/gui.gif" alt="ModbusSniffer GUI demo" />
  <p><em>Live preview of ModbusSniffer GUI in action</em></p>
</div>

---

## 🚀 Why ModbusSniffer (This Fork)?

### 🔍 General Highlights

- 🧰 Sniffs raw Modbus RTU frames from serial ports (RS-485, USB)
- 🖥️ Graphical User Interface (PyQt6) — no terminal needed
- 📋 Frame table: Real-time view with decoded address, function code, and data
- 🌈 Live Logging: Color-coded request–response pairs, unmatched requests highlighted
- 🪟 Cross-platform: Windows & Linux
- 🆓 Free & Open Source (MIT license)

### 🛠️ Why This Fork (What's New)

- 💻 Modular code refactor — clear separation into modules and classes
- 🧠 Rewritten Modbus parser (`ModbusParser` class) with clean structure
- 🖥️ Fully integrated GUI (previously only CLI)
- 🔄 All command-line functionality preserved and upgraded into the GUI

---

## 🆕 What’s New

See the full [CHANGELOG.md](https://github.com/niwciu/ModbusSniffer/blob/main/CHANGELOG.md) for details.

---

## 🔧 ToDo
- Improve GUI with:
  - Add frame filtering
- Add posibility to set log files path 

## 🗺️ Roadmap
- Support for Modbus TCP
- Custom function code decoding
- Advanced filtering and analysis tools
- Plugin system for extensions

## 📚 Documentation & Support

- Detailed documentation will be available in the `docs/` folder soon.
- Questions or issues? Open an [issue](https://github.com/niwciu/ModbusSniffer/issues) or join the [Discussions](https://github.com/niwciu/ModbusSniffer/discussions).

## 🧪 Testing

Run tests with pytest:

```bash
pip install -e .[dev]
pytest
```

Coverage report:
```bash
pytest --cov=modbus_sniffer
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to branch (`git push origin feature-name`)  
5. Open a Pull Request  

After cloning the repository and setting up a virtual environment, you can install all development tools (used in CI/CD pipeline and for local testing, linting, and packaging) with:

```bash
pip install -e .[dev]
```
This includes formatters, linters, type checkers, test runners, and build tools.

---

## 🤝 Acknowledgments

Thanks to the original author [BADAndrea](https://github.com/BADAndrea) for the initial ModbusSniffer implementation.  
Special thanks to all contributors and the open-source community for feedback and improvements.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/niwciu/ModbusSniffer/blob/main/LICENSE) file.

This project is a fork of [BADAndrea ModbusSniffer](https://github.com/BADAndrea/ModbusSniffer)  
Fork maintained by **niwciu** with enhancements described above.

---

❤️ Thank you for using this version of ModbusSniffer!

<div align="center">

---
<img src="https://github.com/user-attachments/assets/f4825882-e285-4e02-a75c-68fc86ff5716" alt="myEmbeddedWayBanerWhiteSmaller"/>

---
</div>