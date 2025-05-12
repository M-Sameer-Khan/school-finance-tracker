from app import app, db
from app.models import User

def verify_admin():
    with app.app_context():
        # Check existing admin
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            print("No admin user found. Creating admin...")
            new_admin = User(
                username='admin', 
                email='admin@school.com', 
                is_admin=True
            )
            new_admin.set_password('SchoolFinance2025!')
            db.session.add(new_admin)
            db.session.commit()
            print("Admin user created successfully!")
        else:
            print("Admin user exists. Verifying password...")
            is_correct = admin.check_password('SchoolFinance2025!')
            print(f"Password check result: {is_correct}")
            
            # Print out user details for debugging
            print(f"Username: {admin.username}")
            print(f"Email: {admin.email}")
            print(f"Is Admin: {admin.is_admin}")

if __name__ == '__main__':
    verify_admin()
