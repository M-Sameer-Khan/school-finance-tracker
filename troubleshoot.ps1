# PowerShell Troubleshooting Script for School Finance Tracker

# Ensure execution policy allows script running
Set-ExecutionPolicy RemoteSigned -Scope Process -Force

# Check Python installation
try {
    $pythonVersion = python --version
    Write-Host "Python installed: $pythonVersion"
} catch {
    Write-Host "Error: Python not found. Please install Python."
    exit 1
}

# Remove existing virtual environment
if (Test-Path -Path "venv") {
    Write-Host "Removing existing virtual environment..."
    Remove-Item -Recurse -Force "venv"
}

# Remove existing database
if (Test-Path -Path "app\school_finance.db") {
    Write-Host "Removing existing database..."
    Remove-Item -Force "app\school_finance.db"
}

# Create new virtual environment
Write-Host "Creating new virtual environment..."
python -m venv venv

# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# Initialize database
Write-Host "Initializing database and creating admin user..."
python init_app.py

# Check log files
if (Test-Path -Path "app.log") {
    Write-Host "=== Application Log ==="
    Get-Content "app.log"
}

if (Test-Path -Path "server.log") {
    Write-Host "=== Server Log ==="
    Get-Content "server.log"
}

# Start the application
Write-Host "Starting School Finance Tracker..."
python run.py

# Pause to keep window open
Read-Host "Press Enter to exit"
