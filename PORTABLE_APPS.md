# Image Processor - Portable Apps Guide

This project includes **two portable applications**:

1. **CLI Application** - Command-line image processor
2. **Web UI Application** - Browser-based image processor with visual interface

Both are standalone executables with **zero dependencies** for Windows and macOS.

---

## 📦 What's Included

### Standalone Executables (Pre-Built)

Available in the `dist/` folder:

```
dist/
├── imageprocessor-macos/
│   ├── imageprocessor       (CLI app - 16 MB)
│   ├── README.md
│   └── LICENSE
│
└── imageprocessor-ui-macos/
    ├── imageprocessor-ui    (Web UI app - 65 MB)
    ├── run.sh
    ├── README.md
    └── LICENSE
```

---

## 🚀 Quick Start

### macOS - CLI Version
```bash
./dist/imageprocessor-macos/imageprocessor image.jpg
./dist/imageprocessor-macos/imageprocessor image.jpg -o output.jpg -c matrix.csv
```

### macOS - Web UI Version
```bash
./dist/imageprocessor-ui-macos/imageprocessor-ui
```
Then open your browser to `http://localhost:8501`

### Windows - CLI Version
```cmd
dist\imageprocessor-windows\imageprocessor.exe image.jpg
dist\imageprocessor-windows\imageprocessor.exe image.jpg -o output.jpg -c matrix.csv
```

### Windows - Web UI Version
```cmd
dist\imageprocessor-ui-windows\imageprocessor-ui.exe
```
Then open your browser to `http://localhost:8501`

---

## 🏗️ Building from Source

### Build CLI Executable

**macOS:**
```bash
chmod +x build_macos.sh
./build_macos.sh
```

**Windows:**
```cmd
build_windows.bat
```

### Build Web UI Executable

**macOS:**
```bash
chmod +x build_ui_macos.sh
./build_ui_macos.sh
```

**Windows:**
```cmd
build_ui_windows.bat
```

---

## 📋 System Requirements

### For Running Pre-Built Executables

**macOS:**
- macOS 10.13 or later
- No additional software needed

**Windows:**
- Windows 7 or later
- No additional software needed

### For Building from Source

**All Platforms:**
- Python 3.8 or higher
- 2 GB free disk space (for build process)

---

## 📤 Distribution

### Package for Distribution

Zip the appropriate folder:

**macOS CLI:**
```bash
cd dist
zip -r imageprocessor-macos.zip imageprocessor-macos/
```

**macOS UI:**
```bash
cd dist
zip -r imageprocessor-ui-macos.zip imageprocessor-ui-macos/
```

**Windows CLI:**
```cmd
cd dist
powershell Compress-Archive imageprocessor-windows imageprocessor-windows.zip
```

**Windows UI:**
```cmd
cd dist
powershell Compress-Archive imageprocessor-ui-windows imageprocessor-ui-windows.zip
```

### Share with Users

1. Zip the executable folder
2. Send the ZIP file
3. Users extract and run:

```bash
# macOS CLI
./imageprocessor image.jpg

# macOS UI
./imageprocessor-ui

# Windows CLI
imageprocessor.exe image.jpg

# Windows UI
imageprocessor-ui.exe
```

---

## 🎯 Use Cases

### CLI Application
- Batch processing via scripts
- Integration into workflows
- Server/automation tasks
- Command-line automation

### Web UI Application
- User-friendly interface
- Real-time preview
- Interactive downloads
- No terminal knowledge required

---

## 🔧 What's Bundled in Executables

Each executable includes:

- ✅ Python 3 runtime
- ✅ Pillow (image processing)
- ✅ NumPy (matrix operations)
- ✅ Streamlit (UI version only)
- ✅ All dependencies
- ✅ Application source code

**No external installation required!**

---

## 📊 File Sizes

| App | OS | Size |
|-----|----|----|
| CLI | macOS | ~16 MB |
| CLI | Windows | ~16 MB |
| UI | macOS | ~65 MB |
| UI | Windows | ~65 MB |

---

## 🐛 Troubleshooting

### "Command not found" on macOS
```bash
chmod +x imageprocessor
./imageprocessor image.jpg
```

### Port 8501 already in use
The web UI uses port 8501. If occupied, kill the process:

**macOS/Linux:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Windows:**
```cmd
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### Build fails
Try rebuilding with a clean virtual environment:

**macOS/Linux:**
```bash
rm -rf venv build dist
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./build_macos.sh  # or build_ui_macos.sh
```

**Windows:**
```cmd
rmdir /s venv build dist
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
build_windows.bat
```

---

## 📄 License

See [LICENSE](LICENSE) file for details.
