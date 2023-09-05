from flask import Flask, render_template, jsonify, request, redirect, url_for, session

application = Flask(__name__)

application.secret_key = "my previous"

JOBS = [
    {
        'id': 1,
        'title': 'Frontend Engineer',
        'location': 'Chennai,India',
        'salary': 'Rs. 2,00,000'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location': 'Mumbai,India',
        'salary': 'Rs. 3,00,000'
    },
    {
        'id': 3,
        'title': 'Cloud Engineer',
        'location': 'Remote',
        'salary': '$120,000'
    },
    {
        'id': 4,
        'title': 'DevOps Engineer',
        'location': 'New York,USA',
        'salary': '$150,000'
    },
]


@application.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@application.route("/logout")
def logout_page():
    return render_template('logout.html')


@application.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


@application.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials.Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello_world'))
    return render_template('login.html', error=error)


@application.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('logout_page'))


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
