#!/bin/bash

# Streamlit Web UI startup script for macOS

echo "Starting Image Processor Web UI..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -q -r requirements.txt

# Start Streamlit
echo "Opening web browser..."
sleep 2 && open http://localhost:8501 &

echo ""
echo "🎉 Image Processor UI is starting!"
echo "📍 Open: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
