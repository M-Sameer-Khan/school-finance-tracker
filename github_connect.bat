@echo off
echo ===================================================
echo School Finance Tracker - GitHub Connection Script
echo ===================================================
echo.
echo This script will connect your local repository to GitHub
echo and push your code to the repository you created.
echo.
echo IMPORTANT: Before continuing, make sure you have:
echo 1. Created a repository named 'school-finance-tracker' on GitHub
echo 2. Your GitHub username is M-Sameer-Khan
echo.
echo If you need to use a different username, edit this script first.
echo.
set /p CONTINUE=Are you ready to continue? (Y/N): 

if /I "%CONTINUE%" NEQ "Y" (
    echo Operation cancelled by user.
    goto :EOF
)

echo.
echo Connecting to GitHub...
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/M-Sameer-Khan/school-finance-tracker.git

echo.
echo Pushing your code to GitHub...
echo (You may be prompted for your GitHub credentials)
echo.
"C:\Program Files\Git\bin\git.exe" push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===================================================
    echo SUCCESS! Your code is now on GitHub!
    echo ===================================================
    echo.
    echo Your repository URL is:
    echo https://github.com/M-Sameer-Khan/school-finance-tracker
    echo.
    echo Next steps for Windsurf integration:
    echo 1. Go to Windsurf and sign in
    echo 2. Create or select a project
    echo 3. Connect your GitHub repository
    echo 4. Complete any required authorization
    echo 5. Configure deployment settings
) else (
    echo.
    echo There was an issue connecting to GitHub.
    echo.
    echo If you're seeing authentication errors, you may need to:
    echo 1. Visit https://github.com/settings/tokens to create a personal access token
    echo 2. Use the token instead of your password when prompted
    echo 3. Make sure your repository exists at GitHub.com/M-Sameer-Khan/school-finance-tracker
)

echo.
echo Press any key to exit...
pause > nul
