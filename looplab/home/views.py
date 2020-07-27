from flask import render_template, request, redirect, url_for

from looplab import app

from .forms import LandingForm, ViewItemsForm
from .models import EmailSignup

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        data = form.data
        data = {
            'full_name': form.full_name.data,
            'email': form.email.data
        }
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        msg = 'Success'
        if obj is None:
            obj = EmailSignup(**data)
            obj.save()
        # return render_template('index.html', message=msg)
        return render_template('success.html', data=data)
    return render_template('index.html', form=form)

@app.route('/success/', methods=['POST'])
def success_view():
    return render_template('success.html')
