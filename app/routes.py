import logging
from flask import render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import app, db
from app.models import User, Income, Expense, Budget
from werkzeug.security import check_password_hash
from werkzeug.exceptions import HTTPException

# Configure logging
logger = logging.getLogger(__name__)

# Global error handler
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    
    logger.error(f'Unhandled Exception: {str(e)}', exc_info=True)
    
    return jsonify(error=str(e)), code

# Catch-all route to handle method not allowed
@app.route('/', methods=['GET', 'POST'])
def catch_all():
    logger.warning(f'Catch-all route hit with method: {request.method}')
    if current_user.is_authenticated:
        total_income = sum(income.amount for income in Income.query.all())
        total_expenses = sum(expense.amount for expense in Expense.query.all())
        return render_template('dashboard.html', 
                               total_income=total_income, 
                               total_expenses=total_expenses)
    return render_template('login.html')
from werkzeug.utils import secure_filename
import os
import openpyxl
from datetime import datetime

@app.route('/')
def index():
    print('Current user:', current_user)
    print('Is authenticated:', getattr(current_user, 'is_authenticated', None))
    if current_user.is_authenticated:
        # Calculate totals for the dashboard
        total_income = sum(income.amount for income in Income.query.all())
        total_expenses = sum(expense.amount for expense in Expense.query.all())
        
        # Get recent incomes and expenses for display
        recent_incomes = Income.query.order_by(Income.date.desc()).limit(5).all()
        recent_expenses = Expense.query.order_by(Expense.date.desc()).limit(5).all()
        
        from datetime import datetime
        current_year = datetime.now().year
        return render_template('dashboard.html', 
                               total_income=total_income, 
                               total_expenses=total_expenses,
                               recent_incomes=recent_incomes,
                               recent_expenses=recent_expenses,
                               now=lambda: datetime.now())
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Don't show login page if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    print(f"\n============= LOGIN ROUTE ==============")
    print(f"Request method: {request.method}")
    print(f"Current user: {current_user}")
    
    try:
        if request.method == 'POST':
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            
            print(f"Login attempt - Username: {username}, Password length: {len(password)}")
            
            if not username or not password:
                flash('Username and password are required', 'danger')
                return render_template('login.html'), 400
            
            # For debugging - verify admin exists
            print("Checking if admin exists...")
            admin_user = User.query.filter_by(username='admin').first()
            if admin_user:
                print(f"Admin user exists - ID: {admin_user.id}, Email: {admin_user.email}")
                print(f"Password hash: {admin_user.password_hash[:10]}...")
            else:
                print("No admin user found in database!")
            
            # Check user
            user = User.query.filter_by(username=username).first()
            
            if not user:
                flash('Invalid username or password', 'danger')
                return render_template('login.html')
            
            # Check password
            is_password_correct = user.check_password(password)
            print(f"Password check result: {is_password_correct}")
            
            if is_password_correct:
                # Login the user with remember=True for persistence
                login_user(user, remember=True)
                print(f"User logged in successfully: {current_user.is_authenticated}")
                
                # Important: Use next_page pattern to handle redirects properly
                next_page = request.args.get('next')
                if not next_page or urlparse(next_page).netloc != '':
                    next_page = url_for('index')
                
                flash('Login successful!', 'success')
                return redirect(next_page)
            else:
                flash('Invalid username or password', 'danger')
        
        # GET request - render the login form
        return render_template('login.html')
    
    except Exception as e:
        print(f"Login error: {str(e)}")
        flash('An unexpected error occurred. Please try again.', 'danger')
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/income', methods=['GET', 'POST'])
@login_required
def manage_income():
    if request.method == 'POST':
        source = request.form['source']
        amount = float(request.form['amount'])
        description = request.form['description']
        
        new_income = Income(source=source, amount=amount, description=description)
        db.session.add(new_income)
        db.session.commit()
        flash('Income added successfully!')
        return redirect(url_for('manage_income'))
    
    incomes = Income.query.order_by(Income.date.desc()).all()
    return render_template('income.html', incomes=incomes)

@app.route('/expenses', methods=['GET', 'POST'])
@login_required
def manage_expenses():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        
        new_expense = Expense(category=category, amount=amount, description=description)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!')
        return redirect(url_for('manage_expenses'))
    
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/budget', methods=['GET', 'POST'])
@login_required
def manage_budget():
    if request.method == 'POST':
        category = request.form['category']
        allocated_amount = float(request.form['allocated_amount'])
        fiscal_year = int(request.form['fiscal_year'])
        description = request.form['description']
        
        new_budget = Budget(category=category, 
                            allocated_amount=allocated_amount, 
                            fiscal_year=fiscal_year, 
                            description=description)
        db.session.add(new_budget)
        db.session.commit()
        flash('Budget added successfully!')
        return redirect(url_for('manage_budget'))
    
    budgets = Budget.query.order_by(Budget.fiscal_year.desc()).all()
    return render_template('budget.html', budgets=budgets)

@app.route('/reports')
@login_required
def financial_reports():
    # Implement financial reporting logic
    incomes = Income.query.all()
    expenses = Expense.query.all()
    budgets = Budget.query.all()
    
    return render_template('reports.html', 
                           incomes=incomes, 
                           expenses=expenses, 
                           budgets=budgets)

@app.route('/import', methods=['GET', 'POST'])
@login_required
def import_excel():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.root_path, 'uploads', filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            file.save(file_path)
            
            try:
                workbook = openpyxl.load_workbook(file_path)
                
                # Import Income
                if 'Income' in workbook.sheetnames:
                    income_sheet = workbook['Income']
                    for row in income_sheet.iter_rows(min_row=2, values_only=True):
                        if row[0]:  # Check if row is not empty
                            new_income = Income(
                                source=str(row[0]),
                                amount=float(row[1]),
                                date=datetime.strptime(str(row[2]), '%Y-%m-%d') if row[2] else datetime.now(),
                                description=str(row[3]) if row[3] else ''
                            )
                            db.session.add(new_income)
                
                # Import Expenses
                if 'Expenses' in workbook.sheetnames:
                    expense_sheet = workbook['Expenses']
                    for row in expense_sheet.iter_rows(min_row=2, values_only=True):
                        if row[0]:  # Check if row is not empty
                            new_expense = Expense(
                                category=str(row[0]),
                                amount=float(row[1]),
                                date=datetime.strptime(str(row[2]), '%Y-%m-%d') if row[2] else datetime.now(),
                                description=str(row[3]) if row[3] else ''
                            )
                            db.session.add(new_expense)
                
                # Import Budget
                if 'Budget' in workbook.sheetnames:
                    budget_sheet = workbook['Budget']
                    for row in budget_sheet.iter_rows(min_row=2, values_only=True):
                        if row[0]:  # Check if row is not empty
                            new_budget = Budget(
                                category=str(row[0]),
                                allocated_amount=float(row[1]),
                                fiscal_year=int(row[2]),
                                description=str(row[3]) if row[3] else ''
                            )
                            db.session.add(new_budget)
                
                db.session.commit()
                flash('Excel file imported successfully!')
            except Exception as e:
                db.session.rollback()
                flash(f'Error importing file: {str(e)}')
            
            # Clean up uploaded file
            os.remove(file_path)
            
            return redirect(url_for('index'))
    
    return render_template('import.html')
