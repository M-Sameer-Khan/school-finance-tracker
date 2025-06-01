Write-Host "\n===== School Finance Tracker - GitHub Setup =====\n" -ForegroundColor Cyan

# Clean up any existing remote
Write-Host "Removing any existing remote connections..." -ForegroundColor Yellow
& "C:\Program Files\Git\bin\git.exe" remote remove origin

# Add the new remote
Write-Host "\nSetting up connection to GitHub..." -ForegroundColor Yellow
& "C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/M-Sameer-Khan/school-finance-tracker.git

Write-Host "\n===== GITHUB AUTHENTICATION =====" -ForegroundColor Magenta
Write-Host "When pushing, you'll need to enter:" -ForegroundColor White
Write-Host "1. Your GitHub username" -ForegroundColor White
Write-Host "2. Your personal access token (NOT your password)" -ForegroundColor White

Write-Host "\nReady to push your code to GitHub" -ForegroundColor Green
Write-Host "Press Enter to continue..." -ForegroundColor Cyan
Read-Host

Write-Host "\nPushing code to GitHub..." -ForegroundColor Yellow
& "C:\Program Files\Git\bin\git.exe" push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "\n===== SUCCESS! =====" -ForegroundColor Green
    Write-Host "Your code is now on GitHub at:" -ForegroundColor Green
    Write-Host "https://github.com/M-Sameer-Khan/school-finance-tracker" -ForegroundColor Cyan
    
    Write-Host "\nNext step: Connect to Windsurf" -ForegroundColor Yellow
    Write-Host "1. Log in to Windsurf" -ForegroundColor White
    Write-Host "2. Create a new project" -ForegroundColor White
    Write-Host "3. Connect to GitHub repository: M-Sameer-Khan/school-finance-tracker" -ForegroundColor White
} else {
    Write-Host "\n===== TROUBLESHOOTING =====" -ForegroundColor Red
    Write-Host "Issue pushing to GitHub. Please check:" -ForegroundColor Red
    Write-Host "1. Have you created the repository on GitHub.com?" -ForegroundColor White
    Write-Host "2. Did you use the correct personal access token?" -ForegroundColor White
    Write-Host "3. Does your token have the 'repo' scope?" -ForegroundColor White
    Write-Host "4. Is your GitHub username correct?" -ForegroundColor White
}

Write-Host "\nPress Enter to exit..." -ForegroundColor Yellow
Read-Host
