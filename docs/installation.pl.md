# Przewodnik Instalacji

Ten przewodnik obejmuje różne sposoby instalacji i uruchomienia ModbusSniffer w Twoim systemie.

## Łatwa Instalacja (Prekompilowane Binaria lub Skrypty Build dla Windows i Linux)

Nie musisz niczego budować ręcznie!  
Ten projekt używa GitHub Actions (GHA) do automatycznego budowania i publikowania zweryfikowanych binariów dla każdej wersji.  
Prekompilowane wersje dla Ubuntu i Windows są dostępne w zakładce [Releases](https://github.com/niwciu/ModbusSniffer/releases).

Aby uzyskać niestandardowe buildy i automatyczne ustawienie skrótów, zobacz sekcję **🛠️ Build & Install** poniżej.

## Build & Install

### 1. Ogólne Wymagania

#### - Python 3 zainstalowany
#### - pip3 zainstalowany

#### 🐧 Linux
```bash
sudo apt install python3-pip
```

#### 🪟 Windows
```powershell
python -m ensurepip --upgrade
```

### 2. Sklonuj Repozytorium

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer/install_scripts
```

### 3. Zbuduj Plik Wykonywalny (dla Ubuntu i Windows)

> **Uwaga:** Jeśli chcesz tylko **uruchomić** aplikację, a nie budować, pomiń ten krok i przejdź do **▶️ Uruchamianie aplikacji GUI bez instalacji**.

#### 🐧 Linux

```bash
sudo chmod +x build.sh
./build.sh
```

> Ten skrypt:
> * Czyści poprzednie pliki build (build/, dist/, .spec, __pycache__/)
> * Tworzy wirtualne środowisko i instaluje zależności
> * Używa PyInstaller do zbudowania aplikacji
> * Dodaje skróty w Menu Start i na pulpicie

#### 🪟 Windows

```powershell
./build.bat
```

> Ten skrypt:
> * Czyści poprzednie pliki build
> * Konfiguruje wirtualne środowisko i instaluje zależności
> * Buduje samodzielny .exe używając PyInstaller
> * Dodaje skróty na pulpicie i w Menu Start

## Uruchamianie Aplikacji GUI (zainstalowanej via pip)

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Utwórz i Aktywuj Wirtualne Środowisko
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

### 3. Zainstaluj pakiet i narzędzia deweloperskie

```bash
pip install -e .[dev]
```

### 4. Uruchom aplikację GUI 🎛️ 🧩
```bash
modbus-sniffer-gui
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne

### 5. Dezaktywuj Wirtualne Środowisko
```bash
deactivate
```

## Uruchamianie Aplikacji CLI (zainstalowanej via pip)

### 1. Sklonuj repozytorium
```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Utwórz i Aktywuj Wirtualne Środowisko

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

### 3. Zainstaluj pakiet i narzędzia deweloperskie

```bash
pip install -e .[dev]
```

### 4. Uruchom pomoc CLI 🖥️

```bash
modbus-sniffer -h
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne.

### 5. Przykład użycia 🧪
Uruchom aplikację sniffer CLI na porcie USB0 z prędkością transmisji 115200 i parzystością none
```bash
modbus-sniffer -p /dev/ttyUSB0 -b 115200 -r none
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne.

### 6. Dezaktywuj Wirtualne Środowisko

```bash
deactivate
```

## Uruchamianie Aplikacji GUI bez instalacji

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Utwórz i Aktywuj Wirtualne Środowisko
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

### 3. Zainstaluj wymagania

```bash
pip install -r ./install_scripts/requirements.txt
```

### 4. Uruchom aplikację GUI 🎛️ 🧩
```bash
cd src/modbus_sniffer
python gui.py
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne

### 5. Dezaktywuj Wirtualne Środowisko
```bash
deactivate
```

## Uruchamianie Aplikacji CLI bez instalacji

### 1. Sklonuj repozytorium
```bash
git clone https://github.com/niwciu/ModbusSniffer.git
cd ModbusSniffer
```

### 2. Utwórz i Aktywuj Wirtualne Środowisko

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

### 3. Zainstaluj wymagania

```bash
pip install -r ./install_scripts/requirements.txt
```

### 4. Uruchom pomoc CLI 🖥️

```bash
cd src/modbus_sniffer
python cli.py -h
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne.

### 5. Przykład użycia 🧪
Uruchom aplikację sniffer CLI na porcie USB0 z prędkością transmisji 115200 i parzystością none
```bash
cd src/modbus_sniffer #opcjonalne - jeśli uruchamiane z głównego folderu projektu
python cli.py -p /dev/ttyUSB0 -b 115200 -r none
```
> Uwaga: wirtualne środowisko (.venv) musi być aktywne.

### 6. Dezaktywuj Wirtualne Środowisko

```bash
deactivate
```

## Rozwiązywanie Problemów

**Problem: Port szeregowy nie znaleziony**  
Upewnij się, że port jest poprawny (np. /dev/ttyUSB0 w Linux, COM3 w Windows). Sprawdź za pomocą `ls /dev/tty*` lub Menedżera Urządzeń.

**Problem: Odmowa dostępu w Linux**  
Dodaj użytkownika do grupy dialout: `sudo usermod -a -G dialout $USER`, następnie uruchom ponownie.

**Problem: PyQt6 nie instaluje się**  
Zainstaluj zależności systemowe: `sudo apt install python3-pyqt6` w Ubuntu.

**Problem: Build kończy się niepowodzeniem**  
Upewnij się, że masz Python 3.8+ i wszystkie zależności. Wyczyść build za pomocą `rm -rf build dist *.spec`.

Aby uzyskać więcej pomocy, sprawdź [GitHub Issues](https://github.com/niwciu/ModbusSniffer/issues).