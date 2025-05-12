# PowerShell script to add Python to system PATH

# Require administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))  
{  
    Write-Warning "Please run this script as an Administrator!"
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Find Python installation
function Find-PythonPath {
    $pythonPaths = @(
        "C:\Python311",
        "C:\Python310", 
        "C:\Python39", 
        "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python3*",
        "C:\Program Files\Python3*",
        "C:\Program Files (x86)\Python3*"
    )

    foreach ($path in $pythonPaths) {
        $fullPath = Resolve-Path $path -ErrorAction SilentlyContinue
        if ($fullPath) {
            $pythonExe = Get-ChildItem -Path $fullPath -Filter "python.exe" -Recurse | Select-Object -First 1
            if ($pythonExe) {
                return $pythonExe.DirectoryName
            }
        }
    }
    return $null
}

# Get Python path
$pythonPath = Find-PythonPath

if ($pythonPath) {
    # Get current PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

    # Check if Python path already exists
    if ($currentPath -notlike "*$pythonPath*") {
        # Add Python path and Scripts directory to PATH
        $newPath = $currentPath + ";$pythonPath;$pythonPath\Scripts"
        
        [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
        
        Write-Host "Python path added successfully: $pythonPath"
        Write-Host "Please restart your computer for changes to take effect."
    }
    else {
        Write-Host "Python path already exists in PATH."
    }

    # Verify Python installation
    Write-Host "`nVerifying Python installation..."
    & "$pythonPath\python.exe" --version
    & "$pythonPath\python.exe" -m pip --version
}
else {
    Write-Host "Python installation not found. Please install Python first."
    Write-Host "Download from: https://www.python.org/downloads/windows/"
}

# Pause to view results
Read-Host "Press Enter to exit"
