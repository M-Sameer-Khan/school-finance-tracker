@echo off
echo ========================================
echo Python Installation Troubleshooter
echo ========================================

REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed.
    echo Please install Python from https://www.python.org/downloads/windows/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    start https://www.python.org/downloads/windows/
    exit /b 1
)

REM Disable Windows App Execution Aliases
echo Disabling Windows App Execution Aliases...
powershell -Command "Get-AppxPackage -Name *Python* | Remove-AppxPackage"
powershell -Command "Get-AppxPackage -Name *WindowsStore* | Remove-AppxPackage"

REM Verify Python installation
echo Checking Python installation...
python --version
pip --version

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

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
