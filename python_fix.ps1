# PowerShell script to fix Python installation

# Disable Windows App Execution Aliases
$aliasPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths"
Remove-ItemProperty -Path "$aliasPath\python.exe" -Name "(Default)" -ErrorAction SilentlyContinue
Remove-ItemProperty -Path "$aliasPath\python3.exe" -Name "(Default)" -ErrorAction SilentlyContinue

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
    Write-Host "No Python installation found. Please install Python from python.org"
}

Read-Host "Press Enter to exit"
