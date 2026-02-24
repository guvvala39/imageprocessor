#!/bin/bash

# Build script for macOS Streamlit UI standalone executable
# Usage: ./build_ui_macos.sh

echo "================================"
echo "Building macOS UI App"
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
echo "Building macOS UI executable..."
pyinstaller --onefile \
    --name imageprocessor-ui \
    --console \
    --hidden-import=streamlit \
    --hidden-import=PIL \
    --hidden-import=numpy \
    --hidden-import=src.image_processor \
    --hidden-import=altair \
    --hidden-import=pandas \
    --hidden-import=protobuf \
    --hidden-import=watchdog \
    app.py

# Create distribution folder
echo "Preparing distribution..."
mkdir -p dist/imageprocessor-ui-macos
cp -r dist/imageprocessor-ui dist/imageprocessor-ui-macos/
cp README.md dist/imageprocessor-ui-macos/
cp LICENSE dist/imageprocessor-ui-macos/
cp PACKAGING.md dist/imageprocessor-ui-macos/

# Create run script
cat > dist/imageprocessor-ui-macos/run.sh << 'EOF'
#!/bin/bash
# Open the app
./imageprocessor-ui
EOF
chmod +x dist/imageprocessor-ui-macos/run.sh

echo ""
echo "================================"
echo "Build Complete!"
echo "================================"
echo ""
echo "Executable location:"
echo "  dist/imageprocessor-ui-macos/imageprocessor-ui"
echo ""
echo "To run the app:"
echo "  ./dist/imageprocessor-ui-macos/imageprocessor-ui"
echo ""
echo "The app will open in your browser at http://localhost:8501"
echo ""
