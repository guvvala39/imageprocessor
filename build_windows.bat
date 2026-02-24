@echo off
REM Build script for Windows standalone executable
REM Usage: build_windows.bat

echo ================================
echo Building Windows Standalone App
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
echo Building Windows executable...
pyinstaller --onefile ^
    --name imageprocessor ^
    --console ^
    --hidden-import=PIL ^
    --hidden-import=numpy ^
    --icon=NONE ^
    process_image.py

REM Create distribution folder
echo Preparing distribution...
if not exist "dist\imageprocessor-windows" mkdir dist\imageprocessor-windows
xcopy /E /I /Y dist\imageprocessor.exe dist\imageprocessor-windows\
copy README.md dist\imageprocessor-windows\
copy LICENSE dist\imageprocessor-windows\

echo.
echo ================================
echo Build Complete!
echo ================================
echo.
echo Executable location:
echo   dist\imageprocessor-windows\imageprocessor.exe
echo.
echo Usage:
echo   imageprocessor.exe ^<image_path^> [options]
echo.
echo Options:
echo   -o, --output    Output image path (default: output_grayscale.jpg)
echo   -c, --csv       CSV matrix path (default: grayscale_matrix.csv)
echo.
pause
