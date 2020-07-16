from looplab import app

@app.route('/users/<username>/')
def profile(username):
    return '<h1>Hello, {username}</h1>'.format(username=username)


@app.route('/users/')
def profiles_list():
    return '<h1>List of users</h1>'