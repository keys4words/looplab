from flask import render_template, request
from looplab import app
from .forms import LandingForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        print(form.full_name.data)
        print(form.email.data)
    return render_template('index.html', form=form)
