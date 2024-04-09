from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Dhk, BD',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Raj, BD',
    'salary': '2000$'
}, {
    'id': 3,
    'title': 'Front-end Engineer',
    'location': 'Remote',
    'salary': '3000$'
}, {
    'id': 4,
    'title': 'Back-end Engineer',
    'location': 'Remote',
    'salary': '4000$'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
