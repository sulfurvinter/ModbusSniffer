# Changelog

# v1.0.4 – What’s Changed 🚀

## 🚀 Feature Enhancements
- 📶 Extended baudrate options in GUI combo box to include 230400, 460800, and 921600

## 📚 Documentation Updates
- 📝 Improved Polish documentation pages with standardized emojis and added UI section
- 🖼️ Added application screenshots and fixed main icon references
- 🔄 Reorganized and fixed Polish index page structure
- 📖 General documentation improvements and updates

## 🧪 Test Suite Fixes
- 🐛 Fixed AttributeError in ModbusParser by initializing `bufferIndex` in `__init__`
- 🔧 Updated GUI tests to use correct imports (QStyleOptionViewItem from QtWidgets)
- 🛠️ Added proper mocking for serial.Serial in tests to prevent real hardware access
- ✅ Fixed assertions in parser tests and GUI add_parsed_data method to use safe dict access
- ⚙️ Configured pytest for source coverage instead of installed package

**Full Changelog**: https://github.com/niwciu/ModbusSniffer/compare/v1.0.3...v1.0.4


# v1.0.3 – What’s Changed 🚀

## ⚙️ CI/CD Improvements
- 🛠️ Added new GitHub Actions workflows:
  - **deploy_app_page.yml** for auto-publishing the documentation site  
  - **ci.yml** steps running lint tests and build on every push/pr with additional manual trigger
  - **build_and_release** for build and release binary files for Windows and Ubuntu

## 📦 PyPI Deployment & Project Restructure
- 📂 Reorganized project into **src/** layout and added **pyproject.toml** per Python Packaging User Guide  
- 🧪 Introduced comprehensive test suite covering core functionality  
- 🏷️ Prepared metadata and packaging config for first PyPI release

## 📚 Documentation
- 📁 Split docs into a dedicated **docs/** folder (MkDocs config) and added **CONTRIBUTING.md**  
- 🌐 Added GitHub Pages deployment instructions and static-site build scripts 

## 🛠️ Installation Scripts
- 📦 Moved all installers into **install_scripts/**:
  - Updated Windows `.bat` and Unix `.sh` scripts with improved error handling  
  - Unified install paths and environment-setup steps 

## 📈 CSV Logger Integration
- 📝 Implemented **csv_logger** module to export captured frames and events to CSV witn hew parser (was a TODO in previous release)  
- 🔄 CSV logging can now be enabled via CLI/GUI flags for post-processing and analytics 

**Full Changelog**: https://github.com/niwciu/ModbusSniffer/compare/v1.0.2...v1.0.3


# v1.0.2 –  What's Changed 🚀

## 📦 Build System
- ⚙️ Added cross-platform build scripts for Windows and Ubuntu using GitHub Actions
- 🖥️ Configured PyInstaller with platform-specific settings and application icon

## 🧾 Documentation
- 📚 Updated README with clearer setup and usage instructions
- 📥 Added instructions on downloading prebuilt executables

## 🖼️ Visual Polish
- 🧊 Added custom application icons for Windows and Linux builds

## 📑 Project Management
- 🆕 Introduced structured `CHANGELOG.md` for tracking changes

**Full Changelog**: https://github.com/niwciu/ModbusSniffer/compare/v1.0.1...v1.0.2

</br></br>

# v1.0.1 – What's Changed 🚀

## 🖥️ GUI Improvements
- 🛠️ Reorganized Settings section and updated to use comboboxes
- 🔌 Added auto-detection for serial devices
- 🧹 Introduced Clear View button for quick UI reset
- 🧾 Added data formatting for improved table data presentation

## ⚙️ Modbus Parser Improvements (New Version)
- 🔧 Refactored the module for better standardization and easier future extensibility
- 🐞 Fixed bugs and applied improvements after validating all functions that the parser can interpret

**Full Changelog**: https://github.com/niwciu/ModbusSniffer/compare/v1.0.0...v1.0.1

</br></br>
# v1.0.0 – Initial Release 🎉

This project is a fork of [BADAndrea ModbusSniffer](https://github.com/BADAndrea/ModbusSniffer)

## This version brings:
- 💻 Code Refactor: Modular architecture with clear separation into modules and classes
- 🛠️ Parser Overhaul: Fully rewritten ModbusParser as a dedicated class
- 🖥️ GUI Added: A basic graphical interface for easier use
- 🔄 CLI → GUI: All command-line functionality integrated into the GUI
- 📋 Frame Table: Real-time view of the latest captured frames
- 🌈 Live Logging: Color-coded request–response pairs; unmatched requests highlighted in red

<div align="center">

---
<img src="https://github.com/user-attachments/assets/f4825882-e285-4e02-a75c-68fc86ff5716" alt="myEmbeddedWayBanerWhiteSmaller"/>

---
</div>