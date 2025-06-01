@echo off
echo ===================================================
echo School Finance Tracker - GitHub Push Script
echo ===================================================
echo.

:: Remove existing origin if it exists
echo Cleaning up previous connection attempts...
"C:\Program Files\Git\bin\git.exe" remote remove origin

:: Add the new origin
echo Setting up connection to your GitHub repository...
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/M-Sameer-Khan/school-finance-tracker.git

echo.
echo ===================================================
echo IMPORTANT: Authentication Instructions
echo ===================================================
echo.
echo When prompted for credentials:
echo 1. Username: Enter your GitHub username (M-Sameer-Khan)
echo 2. Password: DO NOT use your regular GitHub password
echo    Instead, use a Personal Access Token from:
echo    https://github.com/settings/tokens
echo.
echo If you haven't created a token yet:
echo 1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
echo 2. Generate new token → Select at least 'repo' scope
echo 3. Copy the token and use it as your password below
echo.
echo Press any key when you're ready to push your code...
pause > nul

echo.
echo Pushing your code to GitHub...
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
) else (
    echo.
    echo There was an issue pushing to GitHub.
    echo.
    echo Possible causes:
    echo 1. The repository doesn't exist yet - create it on GitHub first
    echo 2. Authentication failed - make sure to use a personal access token
    echo 3. GitHub username might be different - edit this script if needed
)

echo.
echo Press any key to exit...
pause > nul
