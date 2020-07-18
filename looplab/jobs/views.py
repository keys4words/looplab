from flask import jsonify

from looplab import app

@app.route('/jobs/')
def jobs_api():
    data = {'job_id': 343, 'tasks':[1, 43, 5, 99]}
    return jsonify(data)

@app.route('/jobs/<job_id>/')
def job_profile(job_id):
    return '<h1>Hello, {job_id}</h1>'.format(job_id=job_id)


# @app.route('/jobs/')
# def jobs_list():
#     return '<h1>List of jobs</h1>'