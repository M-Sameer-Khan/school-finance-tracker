@echo off
setlocal enabledelayedexpansion

echo ========================================
echo School Finance Tracker - Complete Setup
echo ========================================

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python by following the instructions in PYTHON_SETUP.md
    pause
    start notepad PYTHON_SETUP.md
    exit /b 1
)

REM Ensure pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please reinstall Python and ensure pip is selected.
    pause
    exit /b 1
)

REM Create virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip and setuptools
python -m pip install --upgrade pip setuptools

REM Install dependencies
echo Installing project dependencies...
pip install -r requirements.txt

REM Initialize database
echo Initializing database...
python init_app.py

REM Start the application
echo.
echo ========================================
echo School Finance Tracker is ready!
echo.
echo Login Credentials:
echo Username: admin
echo Password: SchoolFinance2025!
echo.
echo Open a web browser and go to: http://localhost:5000
echo ========================================
echo.

python run.py
pause
