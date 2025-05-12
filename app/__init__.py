import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log')

# Initialize core application components
app = Flask(__name__)

# Use a constant secret key for sessions
app.config['SECRET_KEY'] = 'school-finance-tracker-fixed-key-2025'

# Session configuration for stability
app.config['SESSION_PERMANENT'] = True

# Ensure database directory exists
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'school_finance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager with direct app reference
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes and models to avoid circular imports
from app import routes, models

# Create database tables and initial admin user
def create_admin_user():
    try:
        # Check if admin user already exists
        existing_admin = models.User.query.filter_by(username='admin').first()
        if not existing_admin:
            admin = models.User(
                username='admin', 
                email='admin@school.com', 
                is_admin=True
            )
            admin.set_password('SchoolFinance2025!')
            db.session.add(admin)
            db.session.commit()
            logging.info('Admin user created successfully')
        else:
            logging.info('Admin user already exists')
    except Exception as e:
        logging.error(f'Error creating admin user: {e}')
        db.session.rollback()

# Ensure database and admin user are set up
with app.app_context():
    try:
        db.create_all()
        create_admin_user()
    except Exception as e:
        logging.error(f'Database initialization error: {e}')
