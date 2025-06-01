from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    print(f"Loading user with ID: {user_id}")
    user = User.query.get(int(user_id))
    print(f"User loaded: {user is not None}")
    return user

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @classmethod
    def create_admin(cls, username, email, password):
        """
        Create an admin user with the given credentials.
        
        :param username: Admin username
        :param email: Admin email
        :param password: Admin password
        :return: Created admin user
        """
        admin = cls(username=username, email=email, is_admin=True)
        admin.set_password(password)
        return admin

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    allocated_amount = db.Column(db.Float, nullable=False)
    fiscal_year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)


class Student(db.Model):
    """Student model for storing student details"""
    id = db.Column(db.Integer, primary_key=True)
    gr_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(20), nullable=False)
    admission_date = db.Column(db.Date, default=datetime.utcnow)
    
    # Additional fields from the admission form
    nationality = db.Column(db.String(50))
    religion = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date)
    cnic = db.Column(db.String(20))
    address = db.Column(db.String(200))
    
    # Parent/Guardian information
    guardian_type = db.Column(db.String(20)) # Parent or Guardian
    guardian_name = db.Column(db.String(100))
    guardian_relation = db.Column(db.String(50))
    guardian_phone = db.Column(db.String(20))
    guardian_email = db.Column(db.String(100))
    guardian_occupation = db.Column(db.String(100))
    
    # Academic details
    previous_school = db.Column(db.String(200))
    last_exam_passed = db.Column(db.String(100))
    last_exam_marks = db.Column(db.String(20))
    last_exam_grade = db.Column(db.String(10))
    last_exam_year = db.Column(db.String(10))
    transfer_certificate = db.Column(db.Boolean, default=False)
    
    # Relationship with FeePayment
    fee_payments = db.relationship('FeePayment', backref='student', lazy=True)
    
    def __repr__(self):
        return f"Student('{self.name}', '{self.gr_number}', '{self.class_name}')"
    
    def calculate_monthly_fee(self):
        """Calculate monthly fee based on class"""
        high_classes = ['9', '10', '9th Standard', '10th Standard']
        if any(cls in self.class_name for cls in high_classes):
            return 1500
        else:
            return 1200
            
    def get_fee_status(self, month, year):
        """Get fee status for a specific month and year"""
        payment = FeePayment.query.filter_by(
            student_id=self.id,
            month=month,
            year=year
        ).first()
        
        if payment:
            return payment.payment_status
        return "Unpaid"


class FeePayment(db.Model):
    """Fee payment model for storing fee payment details"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, default=datetime.utcnow)
    payment_status = db.Column(db.String(20), default='Unpaid')
    receipt_number = db.Column(db.String(50), nullable=True)
    payment_method = db.Column(db.String(50), default='Cash')
    remarks = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f"FeePayment(Student ID: {self.student_id}, Month: {self.month}/{self.year}, Amount: {self.amount}, Status: {self.payment_status})"
