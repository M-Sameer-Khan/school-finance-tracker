@echo off
echo Connecting to GitHub...
echo.
echo This script will connect your local repository to GitHub
echo.

set /p GITHUB_URL=Enter your GitHub repository URL (https://github.com/M-Sameer-Khan/school-finance-tracker.git): 

echo.
echo Connecting to %GITHUB_URL%...
"C:\Program Files\Git\bin\git.exe" remote add origin %GITHUB_URL%
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
echo Done! Your repository is now on GitHub.
echo.
echo Next steps:
echo 1. Go to Windsurf
echo 2. Create or select a project
echo 3. Connect your GitHub repository
echo 4. Configure deployment settings
echo.
echo Press any key to exit...
pause > nul
