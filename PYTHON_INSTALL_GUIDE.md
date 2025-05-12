# Python Installation Guide for School Finance Tracker

## Windows Installation Steps

### Method 1: Official Python Installer
1. Download Python Installer
   - Go to: https://www.python.org/downloads/windows/
   - Download the latest Python 3.11 installer (64-bit recommended)

2. Run the Installer
   - **CRITICAL STEPS DURING INSTALLATION**:
     * Check "Add Python to PATH" 
     * Select "Install for all users"
     * Choose "Customize installation"
     * Ensure "pip" is selected for installation

3. Verify Installation
   Open Command Prompt and run:
   ```
   python --version
   pip --version
   ```

### Method 2: Microsoft Store
1. Open Microsoft Store
2. Search for "Python"
3. Install the latest Python version
4. Verify installation as in Method 1

### Troubleshooting PATH Issues
If Python is not recognized:
1. Search "Environment Variables" in Windows search
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "System variables", find and edit "Path"
5. Add these entries:
   - `C:\Python311`
   - `C:\Python311\Scripts`

### Common Issues
- Restart computer after installation
- Disable app execution aliases in Windows settings
- Reinstall if partial/broken installation detected

## Need Help?
Contact IT support if you encounter persistent issues.
