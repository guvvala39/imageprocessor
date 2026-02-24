#!/bin/bash

# Build script for macOS standalone executable
# Usage: ./build_macos.sh

echo "================================"
echo "Building macOS Standalone App"
echo "================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Build executable
echo "Building macOS executable..."
pyinstaller --onefile \
    --name imageprocessor \
    --console \
    --hidden-import=PIL \
    --hidden-import=numpy \
    process_image.py

# Create distribution folder
echo "Preparing distribution..."
mkdir -p dist/imageprocessor-macos
cp -r dist/imageprocessor dist/imageprocessor-macos/
cp README.md dist/imageprocessor-macos/
cp LICENSE dist/imageprocessor-macos/

echo ""
echo "================================"
echo "Build Complete!"
echo "================================"
echo ""
echo "Executable location:"
echo "  dist/imageprocessor-macos/imageprocessor"
echo ""
echo "Usage:"
echo "  ./dist/imageprocessor-macos/imageprocessor <image_path> [options]"
echo ""
echo "Options:"
echo "  -o, --output    Output image path (default: output_grayscale.jpg)"
echo "  -c, --csv       CSV matrix path (default: grayscale_matrix.csv)"
echo ""
