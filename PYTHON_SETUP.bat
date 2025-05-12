@echo off
echo ========================================
echo Python Environment Setup
echo ========================================

REM Find Python executable
for %%P in (python.exe) do (
    set "PYTHON_EXE=%%~$PATH:P"
)

if not defined PYTHON_EXE (
    echo Python not found in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    start https://www.python.org/downloads/windows/
    exit /b 1
)

REM Get Python directory
for %%i in ("%PYTHON_EXE%") do set "PYTHON_DIR=%%~dpI"

REM Create virtual environment
echo Creating virtual environment...
"%PYTHON_EXE%" -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Initialize database
echo Initializing database...
python init_app.py

REM Start the application
echo Starting School Finance Tracker...
python run.py

pause
