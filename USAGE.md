# 📦 Portable Apps - How to Use

## 🎯 Two Applications Available

### 1️⃣ **Web UI** (Recommended for Most Users)
- Browser-based interface
- No terminal knowledge required
- Real-time preview
- Click to download
- Portable executable: ~65 MB

### 2️⃣ **Command Line** (For Automation)
- Terminal-based application
- Batch processing capable
- Scriptable
- Portable executable: ~16 MB

---

## 🚀 Running the Applications

### macOS Users

#### Web UI
```bash
# Make executable (first time only)
chmod +x dist/imageprocessor-ui-macos/imageprocessor-ui

# Run
./dist/imageprocessor-ui-macos/imageprocessor-ui
```

Then open: **http://localhost:8501**

#### CLI
```bash
# Make executable (first time only)
chmod +x dist/imageprocessor-macos/imageprocessor

# Run
./dist/imageprocessor-macos/imageprocessor image.jpg
```

---

### Windows Users

#### Web UI
```cmd
dist\imageprocessor-ui-windows\imageprocessor-ui.exe
```

Then open: **http://localhost:8501**

#### CLI
```cmd
dist\imageprocessor-windows\imageprocessor.exe image.jpg
```

---

## 📋 Options

### Web UI Features
- **Upload Image** - Click or drag JPEG/PNG
- **Cropping Control** - Toggle cropping on/off
- **Crop Settings** - Select size (64-1024px) and region (9 positions)
- **View Preview** - See grayscale result
- **Check Data** - Matrix info and sample values
- **Download** - Grayscale image + CSV matrix with one click

### CLI Options

```bash
imageprocessor image.jpg [options]

Options:
  -o, --output FILE      Save processed image as FILE (default: output_grayscale.jpg)
  -c, --csv FILE         Save matrix as CSV FILE (default: grayscale_matrix.csv)
  -s, --size PIXELS      Crop size in pixels (default: 256, no crop by default)
  -r, --region REGION    Crop region (default: center)
                         Options: center, top-center, top-left, top-right,
                                 bottom-center, bottom-left, bottom-right,
                                 center-left, center-right
  -h, --help             Show help
```

**Examples:**
```bash
# Process without cropping (default)
imageprocessor photo.jpg

# Crop 256x256 from center
imageprocessor photo.jpg -s 256 -r center

# Crop 512x512 from top-center
imageprocessor photo.jpg -s 512 -r top-center

# Custom output names
imageprocessor photo.jpg -o result.jpg -c data.csv

# All options combined
imageprocessor photo.jpg -o result.jpg -c data.csv -s 256 -r top-left

# Show help
imageprocessor --help
```

---

## 📤 Distributing Your Apps

### Option 1: Share Individual Files
```bash
# Create ZIP for others
zip -r imageprocessor-ui-macos.zip dist/imageprocessor-ui-macos/

# Users extract and run
./imageprocessor-ui
```

### Option 2: Self-Extracting Installer
Use third-party tools like:
- **macOS:** Create .dmg (Disk Image)
- **Windows:** Create .msi or .exe installer

### Option 3: Cloud Storage
Upload to Dropbox, Google Drive, or GitHub Releases

---

## ✅ System Requirements

| Platform | Requirement |
|----------|-------------|
| **macOS** | 10.13+ |
| **Windows** | 7+ |
| **Storage** | 100 MB free (UI), 20 MB (CLI) |
| **RAM** | 512 MB minimum |
| **Python** | ❌ Not needed! |
| **Dependencies** | ❌ Not needed! |

---

## 🐛 Troubleshooting

### macOS: "Permission denied"
```bash
chmod +x imageprocessor-ui
./imageprocessor-ui
```

### macOS: "Cannot verify developer"
1. Right-click the executable
2. Select "Open"
3. Click "Open" when prompted

### Windows: Antivirus Warning
PyInstaller executables sometimes trigger antivirus alerts (false positive).

**Solution:** Build from source or whitelist the executable

### Port 8501 Already in Use
If another app uses port 8501:

**macOS/Linux:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Windows:**
```cmd
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

---

## 🔨 Building Your Own Version

### Prerequisites
- Python 3.8+
- ~2 GB free space

### Build Steps

**macOS - CLI:**
```bash
chmod +x build_macos.sh
./build_macos.sh
# Output: dist/imageprocessor-macos/imageprocessor
```

**macOS - Web UI:**
```bash
chmod +x build_ui_macos.sh
./build_ui_macos.sh
# Output: dist/imageprocessor-ui-macos/imageprocessor-ui
```

**Windows - CLI:**
```cmd
build_windows.bat
# Output: dist\imageprocessor-windows\imageprocessor.exe
```

**Windows - Web UI:**
```cmd
build_ui_windows.bat
# Output: dist\imageprocessor-ui-windows\imageprocessor-ui.exe
```

---

## 📊 What's Bundled

Each executable includes:
- ✅ Python 3 runtime
- ✅ Pillow (image processing)
- ✅ NumPy (matrix operations)
- ✅ Streamlit (UI app only)
- ✅ All dependencies pre-packaged

**Result:** Run anywhere without installation!

---

## 💡 Tips

### For Best Performance
- Use JPEG images (smaller file size)
- Keep images under 5 MB
- Close other applications for faster processing

### For Batch Processing
Use the CLI version with a shell script:

```bash
#!/bin/bash
for image in *.jpg; do
    ./imageprocessor-ui "$image" -o "output_$image"
done
```

### Customizing the App
Edit the Python source files and rebuild:
- `app.py` - Web UI code
- `process_image.py` - CLI code
- `src/image_processor.py` - Core processing logic

---

## 📞 Support

For issues or questions:
1. Check [README.md](README.md)
2. Check [PORTABLE_APPS.md](PORTABLE_APPS.md)
3. Review error messages carefully
4. Try rebuilding from source

---

**Enjoy your portable Image Processor! 📷**
