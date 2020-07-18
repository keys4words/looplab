from flask import render_template
from looplab import app



@app.route('/contact-us/')
def contact_us():
    return render_template('contact_test.html')

@app.route('/about-us/')
def about_us():
    return '<h1>About Us</h1>'