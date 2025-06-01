@echo off
echo Connecting to GitHub and pushing your School Finance Tracker...

"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/M-Sameer-Khan/school-finance-tracker.git
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
if %ERRORLEVEL% == 0 (
    echo SUCCESS! Your repository is now on GitHub.
    echo.
    echo Next steps for Windsurf integration:
    echo 1. Go to Windsurf and sign in
    echo 2. Create or select a project
    echo 3. Connect your GitHub repository: M-Sameer-Khan/school-finance-tracker
    echo 4. Configure deployment settings
) else (
    echo There was an issue connecting to GitHub.
    echo.
    echo You may need to:
    echo 1. Create the repository on GitHub first: https://github.com/new
    echo 2. Enter your GitHub credentials when prompted
)

echo.
echo Press any key to exit...
pause > nul
