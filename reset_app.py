from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Run this script to reset the database and create a new admin user

def reset_database():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        
        # Create all tables
        db.create_all()
        
        # Create admin user with direct password hashing
        admin = User(
            username='admin',
            email='admin@school.com',
            password_hash=generate_password_hash('SchoolFinance2025!'),
            is_admin=True
        )
        
        # Add and commit
        db.session.add(admin)
        db.session.commit()
        
        print("Database reset complete!")
        print("New admin user created:")
        print("  Username: admin")
        print("  Password: SchoolFinance2025!")

if __name__ == '__main__':
    reset_database()
