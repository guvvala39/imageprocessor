# Cross-Platform Application Packaging Guide

This document explains how to build standalone executables for Windows and macOS.

## Overview

The application is packaged using **PyInstaller**, which bundles Python, all dependencies (Pillow, NumPy), and your code into a single executable. No system Python installation is required to run it.

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)

## Building for macOS

1. **Clone and navigate to the project:**
   ```bash
   cd /path/to/imageprocessor
   ```

2. **Run the build script:**
   ```bash
   chmod +x build_macos.sh
   ./build_macos.sh
   ```

3. **Find your executable:**
   ```
   dist/imageprocessor-macos/imageprocessor
   ```

4. **Run the app:**
   ```bash
   ./dist/imageprocessor-macos/imageprocessor /path/to/image.jpg
   ```

## Building for Windows

1. **Clone and navigate to the project:**
   ```cmd
   cd C:\path\to\imageprocessor
   ```

2. **Run the build script:**
   ```cmd
   build_windows.bat
   ```

3. **Find your executable:**
   ```
   dist\imageprocessor-windows\imageprocessor.exe
   ```

4. **Run the app:**
   ```cmd
   dist\imageprocessor-windows\imageprocessor.exe C:\path\to\image.jpg
   ```

## Command Line Usage

Once built, both executables work identically:

```bash
# Basic usage
imageprocessor image.jpg

# With custom output paths
imageprocessor image.jpg -o output.jpg -c matrix.csv

# Get help
imageprocessor --help
```

### Options:
- `image_path`: Path to input image (required)
- `-o, --output`: Path to save processed image (default: output_grayscale.jpg)
- `-c, --csv`: Path to save grayscale matrix as CSV (default: grayscale_matrix.csv)

## Distribution

After building, you can distribute the executable folder:

**macOS:**
- Zip the `dist/imageprocessor-macos/` folder
- Users extract and run: `./imageprocessor image.jpg`

**Windows:**
- Zip the `dist/imageprocessor-windows/` folder
- Users extract and run: `imageprocessor.exe image.jpg`

## System Requirements

**macOS:**
- macOS 10.13 or later
- No additional dependencies needed

**Windows:**
- Windows 7 or later
- No additional dependencies needed

## Troubleshooting

### "Command not found" on macOS
Make sure the script is executable:
```bash
chmod +x build_macos.sh
```

### Virtual environment issues
Delete and recreate:
```bash
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

### Import errors during build
Ensure all dependencies are listed in `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## Advanced Options

For custom PyInstaller builds, edit `build_executable.spec` or use:

```bash
# macOS with custom options
pyinstaller --onefile \
    --name imageprocessor \
    --console \
    --hidden-import=PIL \
    --hidden-import=numpy \
    --distpath ./dist/custom \
    process_image.py
```

## What's Included

Each executable includes:
- Python 3 runtime
- Pillow (image processing)
- NumPy (matrix operations)
- Your application code
- All dependencies bundled into a single file

No system-wide installation required!
