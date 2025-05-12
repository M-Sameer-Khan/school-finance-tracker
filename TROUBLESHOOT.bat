@echo off
setlocal enabledelayedexpansion

echo ========================================
echo School Finance Tracker - Troubleshooter
echo ========================================

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/windows/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    start https://www.python.org/downloads/windows/
    exit /b 1
)

REM Remove existing virtual environment and database
if exist venv (
    echo Removing existing virtual environment...
    rmdir /s /q venv
)

if exist app\school_finance.db (
    echo Removing existing database...
    del app\school_finance.db
)

REM Create fresh virtual environment
echo Creating new virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Initialize database with verbose output
echo Initializing database and creating admin user...
python init_app.py

REM Check log files for any errors
echo Checking log files...
if exist app.log (
    echo === Application Log ===
    type app.log
)

if exist server.log (
    echo === Server Log ===
    type server.log
)

REM Run the application
echo Starting School Finance Tracker...
python run.py

pause
