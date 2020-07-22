from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
import email_validator

from .models import EmailSignup

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
        obj = EmailSignup.query.filter_by(email=field.data).first()
        if obj is not None:
            msg = 'This email has already been added!'
            raise ValidationError(msg)