
# 🐍 ModbusSniffer – Free Modbus RTU Analyzer with GUI (Python / PyQt6)

A lightweight and user-friendly Modbus RTU sniffer tool with a graphical interface.  
Easily analyze and debug communication between PLCs, HMIs, and other Modbus RTU devices via serial ports.

[![GitHub release](https://img.shields.io/github/v/release/niwciu/ModbusSniffer)](https://github.com/niwciu/ModbusSniffer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/niwciu/ModbusSniffer)](https://github.com/niwciu/ModbusSniffer/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/niwciu/ModbusSniffer)](https://github.com/niwciu/ModbusSniffer/issues)

<div align="center">
<img src="https://niwciu.github.io/ModbusSniffer/gui.gif" alt="Demo" />
</div>

---

## 🔧 Features

- 🧰 Sniffs raw Modbus RTU frames from serial ports (RS-485, USB)
- 🖥️ GUI interface built with PyQt6
- 📋 Frame table: Real-time decoded Modbus traffic
- 🌈 Color-coded logging of request–response frames
- 📁 Custom log file path — pick your own log file via a file chooser dialog
- 💾 Save log buffer to file at any time with a single button click
- 🪟 Cross-platform: Windows & Linux
- 🆓 MIT licensed, open-source

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install modbus-sniffer
```
or download Binary files for Ubuntu and Windows from [here](https://github.com/niwciu/ModbusSniffer/releases).

You can also build and install app from sourcess. [Click here](docs/installation.md) for deatails about it.


---

## ▶️ Usage

### 🎛️ Run GUI:

```bash
modbus-sniffer-gui
```

### 🖥️ Run CLI:
To list all options:
```bash
modbus-sniffer -h
```


Example of runnig sniffer on ttyUSB0 with baud 115200 and no parity:
```bash
modbus-sniffer -p /dev/ttyUSB0 -b 115200 -r none
```

For more usage options, development guide, and installation from source, visit the GitHub repository:

👉 [ModbusSniffer on GitHub](https://github.com/niwciu/ModbusSniffer)

---

## 📂 Log File Control

The GUI provides two log file controls in the Settings area:

- **Log File** field — shows the current log file path. Click **Browse…** to open a file chooser and select where the log file will be written. If left as `(auto-generated)`, a timestamped file is created automatically in the `logs/` folder on each session start.
- **Save Buffer to File** button — opens a file chooser and saves the entire current log view to the chosen file, independent of the live logging setting.

---
## 🤝 Contributing

Please see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for development setup and contribution guidelines.

---

## 📜 License

MIT License — see the [LICENSE](LICENSE) file for details.  
This project is a fork of [BADAndrea ModbusSniffer](https://github.com/BADAndrea/ModbusSniffer), maintained by **niwciu** with enhancements described above.


<div align="center">

---
<img src="https://github.com/user-attachments/assets/f4825882-e285-4e02-a75c-68fc86ff5716" alt="myEmbeddedWayBanerWhiteSmaller"/>

---
</div>