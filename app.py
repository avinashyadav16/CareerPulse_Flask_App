from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'MERN Developer',
        'location': 'Pune, Maharastra',
        'salary': '₹10,00,000'
    },
    {
        'id': 2,
        'title': 'Business Analyst',
        'location': 'Bengaluru, India',
        'salary': '₹15,00,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '₹11,00,000'
    },
    {
        'id': 4,
        'title': 'Market Researcher',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    }
]


@app.route("/")
def client():
    return render_template('home.html', jobs=JOBS)


# RETURNING THE JOBS AS JSON FILE:
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


# on running python app.py
if __name__ == "__main__":
    # run the flask app
    app.run(host='0.0.0.0', debug=True)
