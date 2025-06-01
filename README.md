# School Finance Tracker

## Overview
A comprehensive web application for managing school finances with a beautiful UI. This application helps educational institutions track income, expenses, budgets, generate financial reports, and manage student fees.

![Dashboard Preview](docs/dashboard.png)

## Features
- **User Authentication** - Secure login system for administrative access
- **Income Tracking** - Record and categorize all income sources
- **Expense Management** - Track and organize expenses by category
- **Budget Allocation** - Set and monitor departmental budgets
- **Financial Reporting** - Generate detailed financial reports and summaries
- **Excel Import** - Import financial data from Excel spreadsheets
- **Student Fee Management** - Manage student admission and fee collection

## Technology Stack
- Python with Flask framework
- SQLAlchemy ORM for database management
- Modern UI with Tailwind CSS and Bootstrap
- Responsive design for all devices

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps
1. Clone this repository:
   ```
   git clone https://github.com/M-Sameer-Khan/school-finance-tracker.git
   cd school-finance-tracker
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the setup script:
   ```
   setup_project.bat  # On Windows
   # ./setup_project.sh  # On macOS/Linux
   ```

5. Start the application:
   ```
   python run.py
   ```

6. Access the application in your browser:
   ```
   http://localhost:5000
   ```

### First-time Login
- Username: `admin`
- Password: `SchoolFinance2025!`

## Student Fee Management
- Add students with complete admission form data
- Track fee payments by class and month
- Generate payment receipts and reports
- View student payment history

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Installation Methods

#### Method 1: Automatic Setup (Recommended)
1. Double-click `COMPLETE_SETUP.bat`
2. Follow on-screen instructions

#### Method 2: Manual Setup
1. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Initialize database
```bash
python init_app.py
```

4. Run the application
```bash
python run.py
```

### Troubleshooting Common Issues

#### Startup Problems
- Run `TROUBLESHOOT.bat` to reset and diagnose issues
- Ensure all dependencies are installed
- Check log files: `app.log` and `server.log`

#### Common Errors
1. **Python Not Found**
   - Install Python from https://www.python.org/downloads/
   - Ensure "Add Python to PATH" is checked during installation

2. **Dependency Issues**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Problems**
   - Delete `app/school_finance.db`
   - Run `init_app.py` to recreate

#### Debugging
- Check `app.log` for application errors
- Check `server.log` for server startup issues

#### Need More Help?
- Consult `PYTHON_SETUP.md`
- Contact your IT support

### Quick Run
- Double-click `RUN_APP.bat`
- Follow on-screen instructions
- Application will start automatically
- Open browser and go to `http://localhost:5000`

**IMPORTANT**: Change the default password after first login!

## Security Notes
- Change the secret key in `app/__init__.py`
- Use environment variables for sensitive information

## Technologies Used
- Flask
- SQLAlchemy
- Bootstrap
- Tailwind CSS
- Flask-Login
