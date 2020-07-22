from flask import render_template, request, redirect

from looplab import app

from .forms import LandingForm
from .models import EmailSignup

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        data = form.data
        print(form.data)
        if 'csrf_token' in data:
            del data['csrf_token']
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        if obj is None:
            obj = EmailSignup(**data)
            obj.save()
        return redirect('/item/{}'.format(obj.id))
    return render_template('index.html', form=form)


@app.route('/item/<int:id>/', methods=['GET'])
def item_detail(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template('items/detail.html', instance=instance)


@app.route('/item/<int:id>/update/', methods=['GET', 'POST'])
def item_update(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    form = LandingForm(obj=instance)
    if form.validate_on_submit():
        data = form.data
        print(data)     
    return render_template('items/form.html', instance=instance, form=form)


@app.route('/item/<int:id>/delete/', methods=['GET', 'POST'])
def item_delete(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template('items/detail.html', instance=instance)