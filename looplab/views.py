from flask import render_template
from looplab import app

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/contact-us/')
def contact_us():
    return '<h1>Contact Us</h1>'

@app.route('/about-us/')
def about_us():
    return '<h1>About Us</h1>'