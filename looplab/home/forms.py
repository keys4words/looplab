from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
import email_validator

class LandingForm(FlaskForm):
    full_name = StringField('Full name',
        render_kw={"class": "form-control", "placeholder": 'Full name'},
        validators=[validators.DataRequired(message='You need to input your full name')])
    email = StringField('Email', 
        render_kw={"class": "form-control", "placeholder": 'Your name'},
        validators=[validators.DataRequired(message='You need to input your email name'),
        validators.Email()])

    def validate_email(self, field):
        if field.data.endswith(".edu"):
            raise ValidationError('You cannot use school address for your email')