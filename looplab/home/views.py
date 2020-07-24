from flask import render_template, request, redirect, url_for

from looplab import app

from .forms import LandingForm, ViewItemsForm
from .models import EmailSignup

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        data = form.data
        # print(form.data)
        data = {
            'full_name': form.full_name.data,
            'email': form.email.data
        }
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        msg = 'Success'
        if obj is None:
            obj = EmailSignup(**data)
            obj.save()
        return render_template('index.html', message=msg)
    return render_template('index.html', form=form)

@app.route('/items/', methods=['GET', 'POST'])
def item_list():
    form = ViewItemsForm()
    if form.validate_on_submit():
        object_list = EmailSignup.query.all()
        return render_template('items/list.html', form=None, object_list=object_list)
    return render_template('items/list.html', form=form, object_list=[])


# @app.route('/item/', methods=['GET'])
# def item_list_redirect():
#     redirect_url = url_for('item_list')
#     return redirect(redirect_url)


# @app.route('/item/<int:id>/', methods=['GET'])
# def item_detail(id):
#     instance = EmailSignup.query.filter_by(id=id).first_or_404()
#     return render_template('items/detail.html', instance=instance)


# @app.route('/items/<int:id>/', methods=['GET'])
# def item_detail_redirect(id):
#     redirect_url = url_for('item_detail', id=id)
#     return redirect(redirect_url)


# @app.route('/item/<int:id>/update/', methods=['GET', 'POST'])
# def item_update(id):
#     # instance = EmailSignup.query.get(id)
#     instance = EmailSignup.query.filter_by(id=id).first_or_404()
#     form = LandingForm(obj=instance)
#     if form.validate_on_submit():
#         full_name = form.full_name.data
#         email = form.email.data
#         instance.full_name = full_name
#         instance.email = email
#         instance.save()
#         return redirect("/item/{}/".format(instance.id))
#     return render_template('items/form.html', instance=instance, form=form)


# @app.route('/item/<int:id>/delete/', methods=['GET', 'POST'])
# def item_delete(id):
#     instance = EmailSignup.query.filter_by(id=id).first_or_404()
#     if request.method == 'POST':
#         instance.delete()
#         return redirect('/')
#     return render_template('items/delete.html', instance=instance)