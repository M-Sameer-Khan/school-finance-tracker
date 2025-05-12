@echo off
echo Setting up School Finance Tracker Project

REM Check if Python is installed
python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please download and install Python from https://www.python.org/downloads/windows/
    pause
    exit /b
)

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Initialize database and create admin user
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
