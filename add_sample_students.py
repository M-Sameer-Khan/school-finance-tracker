from app import app, db
from app.models import Student, FeePayment
from datetime import datetime, timedelta
import random

def add_sample_students():
    """Add sample students based on YES Schooling System admission form format"""
    with app.app_context():
        # Check if we already have students
        existing_count = Student.query.count()
        if existing_count > 0:
            print(f"Database already has {existing_count} students. Skipping sample data creation.")
            return

        # Sample data for various class levels
        classes = [
            "Montessori/P.G", "KG-I", "KG-II",  # Pre-Primary
            "1st Standard", "2nd Standard", "3rd Standard", "4th Standard", "5th Standard",  # Primary
            "6th Standard", "7th Standard", "8th Standard", "9th Standard"  # Secondary
        ]
        
        religions = ["Islam", "Christianity", "Other"]
        genders = ["Male", "Female"]
        guardian_types = ["PARENT", "GUARDIAN"]
        occupations = ["Govt.", "Private", "Business"]
        
        # Create 20 sample students
        students = []
        for i in range(1, 21):
            # Generate GR number
            gr_number = f"GR-{2025}-{1000 + i}"
            
            # Basic student info
            class_name = random.choice(classes)
            gender = random.choice(genders)
            religion = random.choice(religions)
            
            # Create sample student
            student = Student(
                gr_number=gr_number,
                name=f"Student {i}",
                father_name=f"Father of Student {i}",
                class_name=class_name,
                admission_date=datetime.now() - timedelta(days=random.randint(1, 365)),
                nationality="Pakistani",
                religion=religion,
                gender=gender,
                dob=datetime(2010 - random.randint(5, 15), random.randint(1, 12), random.randint(1, 28)),
                cnic=f"12345-{1234567+i}-{i%10}",
                address=f"Plot no: {i}, Kai Mohammad Goth, Layari, Tehsor Town, Karachi",
                
                # Guardian information
                guardian_type=random.choice(guardian_types),
                guardian_name=f"Guardian of Student {i}",
                guardian_relation="Father" if random.random() > 0.3 else "Mother",
                guardian_phone=f"0311-{2000000+i}",
                guardian_email=f"guardian{i}@example.com",
                guardian_occupation=random.choice(occupations),
                
                # Academic details
                previous_school="Previous School Name" if random.random() > 0.5 else None,
                last_exam_passed="Annual Exam 2024" if random.random() > 0.3 else None,
                last_exam_marks=str(random.randint(60, 95)) if random.random() > 0.3 else None,
                last_exam_grade=random.choice(["A", "B", "C"]) if random.random() > 0.3 else None,
                last_exam_year="2024" if random.random() > 0.3 else None,
                transfer_certificate=random.random() > 0.7
            )
            
            db.session.add(student)
            students.append(student)
            print(f"Added student: {student.name}, Class: {student.class_name}")
            
        # Commit students first to get their IDs
        db.session.commit()
        print(f"Committed {len(students)} students to database.")
        
        # Now add fee payments after students have IDs
        for student in students:
            # Add some fee payments for this student
            current_month = datetime.now().month
            current_year = datetime.now().year
            
            # Add payments for past few months (some paid, some partial, some unpaid)
            for month_offset in range(5):
                month = ((current_month - month_offset - 1) % 12) + 1  # Go back in time
                year = current_year if month <= current_month else current_year - 1
                
                # Calculate monthly fee
                monthly_fee = student.calculate_monthly_fee()
                
                # Randomize payment status
                rand = random.random()
                if rand > 0.7:  # 30% unpaid
                    continue  # Skip this month - no payment record means unpaid
                elif rand > 0.3:  # 40% fully paid
                    amount = monthly_fee
                    status = "Paid"
                else:  # 30% partially paid
                    amount = round(monthly_fee * random.uniform(0.3, 0.8))
                    status = "Partially Paid"
                
                # Create payment record
                payment = FeePayment(
                    student_id=student.id,
                    month=month,
                    year=year,
                    amount=amount,
                    payment_date=datetime(year, month, random.randint(1, 28)),
                    payment_status=status
                )
                
                db.session.add(payment)
                print(f"  Added {status} payment for {student.name}: ${amount} for {month}/{year}")
        
        # Commit all fee payments
        db.session.commit()
        print(f"Successfully added sample students with their fee payment history!")

if __name__ == "__main__":
    add_sample_students()
