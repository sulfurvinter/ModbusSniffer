# Installation Guide

This guide covers various ways to install and run ModbusSniffer on your system.

## 🧰 Easy Installation (Pre-built Binaries or Install Scripts for Windows and Linux)

You don't need to build anything manually!  
This project uses GitHub Actions (GHA) to automatically build and publish verified binaries for each release.  
Pre-built versions for Windows and Ubuntu are available under the [Releases](https://github.com/niwciu/ModbusSniffer/releases) tab.

For custom builds and automatic shortcut setup, see the **🛠️ Build & Install** section below.

## 🛠️ Build & Install

### 1. General Requirements

#### - Python 3 installed
#### - pip3 installed

#### 🐧 Linux
```bash
sudo apt install python3-pip
```

#### 🪟 Windows
```powershell
python -m ensurepip --upgrade
```

### 2. Clone the Repository

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer/install_scripts
```

### 3. Build Executable (for Ubuntu and Windows)

> **Note:** If you only want to **run** the app and not build it, skip this step and go to **▶️ Running GUI app without build**.

#### 🐧 Linux

```bash
sudo chmod +x build.sh
./build.sh
```

> This script:
> * Cleans previous build files (build/, dist/, .spec, \_\_pycache\_\_)
> * Creates a virtual environment and installs dependencies
> * Uses PyInstaller to build the app
> * Adds Start Menu and desktop shortcuts

#### 🪟 Windows

```powershell
./build.bat
```

> This script:
> * Cleans previous build files
> * Sets up a virtual environment and installs dependencies
> * Builds a standalone `.exe` using PyInstaller
> * Adds desktop and Start Menu shortcuts

## ▶️ Running GUI App (installed via pip)

### 1. Clone repository

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Create and Activate Virtual Environment
#### 🐧 Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install package and development tools

```bash
pip install -e .[dev]
```

### 4. Run GUI app 🎛️ 🧩
```bash
modbus-sniffer-gui
```
> Note: virtual environment (.venv) must be active

### 5. Deactivate Virtual Environment
```bash
deactivate
```

## 🎮 Running the CLI App (installed via pip)

### 1. Clone repository
```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Create and Activate Virtual Environment

#### 🐧 Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install package and development tools

```bash
pip install -e .[dev]
```

### 4. Run CLI Help 🖥️

```bash
modbus-sniffer -h
```
> Note: virtual environment (.venv) must be active.

### 5. Example of usage 🧪
Run modbus-sniffer CLI app on port USB0 with baud 115200 and parity=none
```bash
modbus-sniffer -p /dev/ttyUSB0 -b 115200 -r none
```
> Note: virtual environment (.venv) must be active.

### 6. Deactivate Virtual Environment

```bash
deactivate
```

## ▶️ Running GUI App without installation

### 1. Clone repository

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Create and Activate Virtual Environment
#### 🐧 Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install requirements

```bash
pip install -r ./install_scripts/requirements.txt
```

### 4. Run GUI app 🎛️ 🧩
```bash
cd src/modbus_sniffer
python gui.py
```
> Note: virtual environment (.venv) must be active

### 5. Deactivate Virtual Environment
```bash
deactivate
```

## 🎮 Running the CLI App without installation

### 1. Clone repository
```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Create and Activate Virtual Environment

#### 🐧 Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install requirements

```bash
pip install -r ./install_scripts/requirements.txt
```

### 4. Run CLI Help 🖥️

```bash
cd src/modbus_sniffer
python cli.py -h
```
> Note: virtual environment (.venv) must be active.

### 5. Example of usage 🧪
Run modbus-sniffer CLI app on port USB0 with baud 115200 and parity=none
```bash
cd src/modbus_sniffer #optional - if running from project main folder
python cli.py -p /dev/ttyUSB0 -b 115200 -r none
```
> Note: virtual environment (.venv) must be active.

### 6. Deactivate Virtual Environment

```bash
deactivate
```