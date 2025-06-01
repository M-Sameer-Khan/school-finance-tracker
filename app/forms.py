from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, BooleanField, SubmitField, FloatField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Optional, Length, EqualTo, ValidationError
from app.models import Student

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AdmissionForm(FlaskForm):
    # Basic Student Information
    gr_number = StringField('G.R Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    father_name = StringField('Father Name', validators=[DataRequired(), Length(min=2, max=100)])
    
    # Class Selection
    class_choices = [
        ('Pre-Primary', (
            ('Montessori/P.G', 'Montessori/P.G'),
            ('KG-I', 'KG-I'),
            ('KG-II', 'KG-II')
        )),
        ('Primary', (
            ('1st Standard', '1st Standard'),
            ('2nd Standard', '2nd Standard'),
            ('3rd Standard', '3rd Standard'),
            ('4th Standard', '4th Standard'),
            ('5th Standard', '5th Standard')
        )),
        ('Secondary', (
            ('6th Standard', '6th Standard'),
            ('7th Standard', '7th Standard'),
            ('8th Standard', '8th Standard'),
            ('9th Standard', '9th Standard'),
            ('10th Standard', '10th Standard')
        ))
    ]
    
    class_name = SelectField('Class', choices=class_choices, validators=[DataRequired()])
    
    # Personal Information
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[Optional()])
    religion = SelectField('Religion', choices=[
        ('Islam', 'Islam'),
        ('Christianity', 'Christianity'),
        ('Other', 'Other')
    ], default='Islam')
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    cnic = StringField('CNIC/Bay-Form', validators=[Optional()])
    address = TextAreaField('Present Address', validators=[DataRequired()])
    
    # Guardian Information
    guardian_type = SelectField('Guardian Type', choices=[
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian')
    ], default='Parent')
    guardian_name = StringField('Guardian Name', validators=[DataRequired()])
    guardian_relation = StringField('Relation', validators=[Optional()])
    guardian_phone = StringField('Cell #', validators=[DataRequired()])
    guardian_email = StringField('E-mail', validators=[Optional(), Email()])
    guardian_occupation = SelectField('Employed', choices=[
        ('Govt.', 'Govt.'),
        ('Private', 'Private'),
        ('Business', 'Business')
    ], validators=[Optional()])
    
    # Academic Record
    previous_school = StringField('Name of School Last Attended', validators=[Optional()])
    last_exam_passed = StringField('Last Exam Passed', validators=[Optional()])
    last_exam_marks = StringField('Marks Obtained', validators=[Optional()])
    last_exam_grade = StringField('Grade', validators=[Optional()])
    last_exam_year = StringField('Year', validators=[Optional()])
    transfer_certificate = BooleanField('Transfer Certificate (T.C.)')
    
    # Documentation
    student_pictures = BooleanField('2 Pictures of Student (1.5"×1.5")')
    previous_result = BooleanField('1 Photocopy of Previous Result Card')
    student_cnic = BooleanField('1 Photocopy of Student\'s Bay-Form')
    father_cnic = BooleanField('1 Photocopy of Father\'s/Guardian\'s CNIC')
    transfer_certificate_doc = BooleanField('1 Photocopy & Original Transfer Certificate(TC) of Last School')
    
    submit = SubmitField('Submit Application')
    
    def validate_gr_number(self, gr_number):
        student = Student.query.filter_by(gr_number=gr_number.data).first()
        if student:
            raise ValidationError('This GR Number is already registered. Please use a different one.')


class FeePaymentForm(FlaskForm):
    student = SelectField('Select Student', validators=[DataRequired()], coerce=int)
    month = SelectField('Month', choices=[
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ], validators=[DataRequired()], coerce=int)
    year = IntegerField('Year', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    payment_date = DateField('Payment Date', format='%Y-%m-%d', validators=[DataRequired()])
    payment_status = SelectField('Payment Status', choices=[
        ('Paid', 'Paid'),
        ('Partially Paid', 'Partially Paid'),
        ('Unpaid', 'Unpaid')
    ], validators=[DataRequired()])
    payment_method = SelectField('Payment Method', choices=[
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cheque', 'Cheque')
    ], default='Cash')
    receipt_number = StringField('Receipt Number', validators=[Optional()])
    remarks = TextAreaField('Remarks', validators=[Optional()])
    
    submit = SubmitField('Record Payment')


class StudentSearchForm(FlaskForm):
    search_query = StringField('Search by Name or GR Number', validators=[DataRequired()])
    submit = SubmitField('Search')


class MonthlyFeeReportForm(FlaskForm):
    month = SelectField('Month', choices=[
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ], validators=[DataRequired()], coerce=int)
    year = IntegerField('Year', validators=[DataRequired()])
    class_filter = SelectField('Filter by Class', validators=[Optional()])
    submit = SubmitField('Generate Report')
