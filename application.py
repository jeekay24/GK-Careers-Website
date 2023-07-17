from flask import Flask, render_template, jsonify

application = Flask(__name__)

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


@application.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
