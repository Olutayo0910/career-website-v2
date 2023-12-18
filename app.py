from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': 'NGN 500,000'
  },
  {
    'title': 'Software Engineer',
    'location': 'London',
    'salary': 'NGN 750,000'
  },
  {
    'title': 'Data Analyst',
    'location': 'Tokyo',
    'salary': 'NGN 1,000,000'
  },
  {
    'title': 'Data Engineer',
    'location': 'Singapore',
    'salary': 'NGN 2,000,000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company='Linters')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
