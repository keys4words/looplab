from flask import render_template

from looplab import app

@app.route('/users/<username>/')
def profile(username):
    return render_template('profile_detail_test.html', username=username)


@app.route('/users/')
def profiles_list():
    show_flag = False
    users_list = ['James Bond', 'Terminator T-1000', 'Kameron Diaz']
    context = dict()
    if show_flag:
        context['users_list'] = users_list
    else:
        context['users_list'] = ['There is not users in the list']

    return render_template('profile_list_test.html', context=context)