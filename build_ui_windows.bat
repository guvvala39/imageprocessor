@echo off
REM Build script for Windows Streamlit UI standalone executable
REM Usage: build_ui_windows.bat

echo ================================
echo Building Windows UI App
echo ================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Build executable
echo Building Windows UI executable...
pyinstaller --onefile ^
    --name imageprocessor-ui ^
    --console ^
    --hidden-import=streamlit ^
    --hidden-import=PIL ^
    --hidden-import=numpy ^
    --hidden-import=src.image_processor ^
    --hidden-import=altair ^
    --hidden-import=pandas ^
    --hidden-import=protobuf ^
    --hidden-import=watchdog ^
    app.py

REM Create distribution folder
echo Preparing distribution...
if not exist "dist\imageprocessor-ui-windows" mkdir dist\imageprocessor-ui-windows
xcopy /E /I /Y dist\imageprocessor-ui.exe dist\imageprocessor-ui-windows\
copy README.md dist\imageprocessor-ui-windows\
copy LICENSE dist\imageprocessor-ui-windows\
copy PACKAGING.md dist\imageprocessor-ui-windows\

REM Create run script
(
echo @echo off
echo imageprocessor-ui.exe
echo pause
) > dist\imageprocessor-ui-windows\run.bat

echo.
echo ================================
echo Build Complete!
echo ================================
echo.
echo Executable location:
echo   dist\imageprocessor-ui-windows\imageprocessor-ui.exe
echo.
echo To run the app:
echo   imageprocessor-ui.exe
echo.
echo The app will open in your browser at http://localhost:8501
echo.
pause
