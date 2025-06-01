Write-Host "\n===== School Finance Tracker - GitHub Fix =====\n" -ForegroundColor Cyan

# Step 1: Pull from remote first (with --allow-unrelated-histories flag)
Write-Host "Step 1: Pulling from GitHub repository..." -ForegroundColor Yellow
Write-Host "This will merge any files that exist on GitHub with your local code" -ForegroundColor Yellow
& "C:\Program Files\Git\bin\git.exe" pull origin main --allow-unrelated-histories

if ($LASTEXITCODE -ne 0) {
    Write-Host "\nPull failed. This might be due to conflict between GitHub and local files." -ForegroundColor Red
    Write-Host "Let's try an alternate approach..." -ForegroundColor Yellow
    
    # Step 2: Force push (if pull fails)
    Write-Host "\nStep 2: Force pushing your code to GitHub..." -ForegroundColor Yellow
    Write-Host "This will overwrite what's on GitHub with your local code" -ForegroundColor Yellow
    Write-Host "Press Enter to continue with force push..." -ForegroundColor Magenta
    Read-Host
    
    & "C:\Program Files\Git\bin\git.exe" push -u origin main --force
} else {
    # Step 3: Normal push (if pull succeeds)
    Write-Host "\nStep 2: Pushing your code to GitHub..." -ForegroundColor Yellow
    & "C:\Program Files\Git\bin\git.exe" push -u origin main
}

# Final result check
if ($LASTEXITCODE -eq 0) {
    Write-Host "\n===== SUCCESS! =====" -ForegroundColor Green
    Write-Host "Your School Finance Tracker is now on GitHub at:" -ForegroundColor Green
    Write-Host "https://github.com/M-Sameer-Khan/school-finance-tracker" -ForegroundColor Cyan
    
    Write-Host "\nNext step: Connect to Windsurf" -ForegroundColor Yellow
    Write-Host "1. Log in to Windsurf" -ForegroundColor White
    Write-Host "2. Create a new project" -ForegroundColor White
    Write-Host "3. Connect to GitHub repository: M-Sameer-Khan/school-finance-tracker" -ForegroundColor White
} else {
    Write-Host "\n===== NEED HELP? =====" -ForegroundColor Red
    Write-Host "If you're still having issues, try these steps:" -ForegroundColor Red
    Write-Host "1. Go to GitHub.com and delete the repository" -ForegroundColor White
    Write-Host "2. Create a new empty repository (no README, no license)" -ForegroundColor White
    Write-Host "3. Run this script again" -ForegroundColor White
}

Write-Host "\nPress Enter to exit..." -ForegroundColor Yellow
Read-Host
