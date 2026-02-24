@echo off
REM Streamlit Web UI startup script for Windows

echo Starting Image Processor Web UI...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
pip install -q -r requirements.txt

echo.
echo Launching web browser...
timeout /t 2 /nobreak

REM Start Streamlit and open browser
start http://localhost:8501
streamlit run app.py
