# PowerShell script to diagnose and fix Python installation

# Require administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))  
{  
    Write-Warning "Please run this script as an Administrator!"
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Disable Windows App Execution Aliases
$aliasPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths"
Remove-ItemProperty -Path "$aliasPath\python.exe" -Name "(Default)" -ErrorAction SilentlyContinue
Remove-ItemProperty -Path "$aliasPath\python3.exe" -Name "(Default)" -ErrorAction SilentlyContinue

# Diagnostic Information
Write-Host "=== Python Diagnostic Information ==="
Write-Host "Checking Python installations..."

# Find Python installations
$pythonPaths = @(
    "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python3*",
    "C:\Python3*",
    "C:\Program Files\Python3*",
    "C:\Program Files (x86)\Python3*"
)

$pythonPath = $null
foreach ($path in $pythonPaths) {
    $foundPath = Resolve-Path $path -ErrorAction SilentlyContinue
    if ($foundPath) {
        $pythonExe = Get-ChildItem -Path $foundPath -Filter "python.exe" -Recurse | Select-Object -First 1
        if ($pythonExe) {
            $pythonPath = $pythonExe.DirectoryName
            break
        }
    }
}

if ($pythonPath) {
    Write-Host "Python found at: $pythonPath"
    
    # Add to system PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    if ($currentPath -notlike "*$pythonPath*") {
        $newPath = $currentPath + ";$pythonPath;$pythonPath\Scripts"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
        Write-Host "Added to PATH: $pythonPath"
    }

    # Verify Python
    & "$pythonPath\python.exe" --version
    & "$pythonPath\python.exe" -m pip --version
}
else {
    Write-Host "No Python installation found."
    Write-Host "Please download from: https://www.python.org/downloads/windows/"
    Start-Process "https://www.python.org/downloads/windows/"
}

Write-Host "`nTroubleshooting Steps:"
Write-Host "1. Ensure Python is installed from python.org"
Write-Host "2. Check 'Add Python to PATH' during installation"
Write-Host "3. Disable Windows App Execution Aliases"

Read-Host "Press Enter to exit"
