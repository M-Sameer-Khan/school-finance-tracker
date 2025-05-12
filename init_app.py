from app import app, db
from app.models import User

def init_db():
    """Initialize the database and create admin user."""
    # Create all database tables
    with app.app_context():
        # Drop existing tables (optional, remove in production)
        db.drop_all()
        
        # Create new tables
        db.create_all()
        
        # Create admin user
        admin_username = 'admin'
        admin_email = 'admin@school.com'
        admin_password = 'SchoolFinance2025!'
        
        # Check if admin user already exists
        existing_admin = User.query.filter_by(username=admin_username).first()
        if not existing_admin:
            admin = User.create_admin(admin_username, admin_email, admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f"Admin user '{admin_username}' created successfully!")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    init_db()
