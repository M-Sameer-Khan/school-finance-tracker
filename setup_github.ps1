# PowerShell script to set up GitHub repository

# Repository information
$repoName = "school-finance-tracker"
$repoDescription = "A comprehensive web application for managing school finances"
$username = "M-Sameer-Khan"

Write-Host "\nSetting up GitHub repository: $repoName" -ForegroundColor Cyan

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git is not installed or not in PATH. Please install Git from https://git-scm.com/download/win" -ForegroundColor Red
    Write-Host "After installing Git, please restart this script." -ForegroundColor Yellow
    exit 1
}

# Initialize git repository
Write-Host "\nInitializing Git repository..." -ForegroundColor Cyan
git init
git add .

# Make initial commit
Write-Host "\nMaking initial commit..." -ForegroundColor Cyan
git commit -m "Initial commit"

# Instructions for manual steps
Write-Host "\n=============================================" -ForegroundColor Yellow
Write-Host "MANUAL STEPS REQUIRED" -ForegroundColor Yellow
Write-Host "=============================================" -ForegroundColor Yellow

Write-Host "\n1. Create a new repository on GitHub:" -ForegroundColor White
Write-Host "   - Go to: https://github.com/new" -ForegroundColor White
Write-Host "   - Repository name: $repoName" -ForegroundColor White
Write-Host "   - Description: $repoDescription" -ForegroundColor White
Write-Host "   - Choose Public or Private" -ForegroundColor White
Write-Host "   - Do NOT initialize with README, .gitignore, or license" -ForegroundColor White
Write-Host "   - Click 'Create repository'" -ForegroundColor White

Write-Host "\n2. After creating the repository, run these commands:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/$username/$repoName.git" -ForegroundColor Green
Write-Host "   git branch -M main" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green

Write-Host "\n3. To connect with Windsurf:" -ForegroundColor White
Write-Host "   - Log into Windsurf" -ForegroundColor White
Write-Host "   - Create a new project or select existing one" -ForegroundColor White
Write-Host "   - Connect GitHub repository: $username/$repoName" -ForegroundColor White
Write-Host "   - Follow authentication prompts" -ForegroundColor White
Write-Host "   - Configure deployment settings" -ForegroundColor White

Write-Host "\nPress Enter to continue..." -ForegroundColor Cyan
Read-Host
