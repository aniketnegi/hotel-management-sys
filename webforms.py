from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


# Maybe add room preference and all, but meh
class reservationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10)])
    address = StringField('Address', validators=[DataRequired()])  # ======Make this a dropdown menu
    id_type = SelectField('ID Type', choices=[('A', 'Aadhar Card'), ('P', 'Passport'), ('', 'PAN Card')], validators=[DataRequired()])
    id_number = StringField('ID Number', validators=[DataRequired()])
    arrival_date = DateField('Arrival Date', validators=[DataRequired()])
    departure_date = DateField('Departure Date', validators=[DataRequired()])
    no_children = IntegerField('No. of Children', validators=[DataRequired()])
    no_adults = IntegerField('No. of Adults', validators=[DataRequired()])
    room_preference = SelectField('Room Preference', choices=[('1', 'Deluxe Room'), ('2', 'Single Room'), ('3', 'Family Room'), ('4', 'Twin Bed Room'), ("NULL", 'No Preference')], validators=[DataRequired()])
    comments = TextAreaField('Comments')
    submit = SubmitField('BOOK NOW')


class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class searchReservation(FlaskForm):
    search_by = SelectField('Search By', choices=[('booking_id', "Booking ID"), ('name', 'Name'), ('email', 'Email'), ('contact_no', 'Phone')], validators=[DataRequired()])
    search_value = StringField('Enter Value', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class confirmReservation(FlaskForm):
    delete = SubmitField('Delete')
    edit = SubmitField('Edit')
    confirm = SubmitField('Confirm')
    