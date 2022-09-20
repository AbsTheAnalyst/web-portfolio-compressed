from flask import Flask, render_template, request, url_for, redirect
from redis import Redis


app = Flask(__name__)

# Page visit counter
redis = Redis(host='redis', port=6379)




@app.route('/')
def home():
    # Counter of Page visit
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    # counter = 1050
    return render_template("index.html", count=counter)


@app.route('/skills/<num>')
def skills(num):

    # counts = request.args
    # counts = counts.to_dict()
    # counts = counts.get("count")

    return render_template("skills.html", count=num)


@app.route('/experience/<num>')
def experience(num):
    return render_template("experience.html", count=num)


@app.route('/education/<num>')
def education(num):
    return render_template("education.html", count=num)


@app.route('/certificates/<num>')
def certificates(num):
    return render_template("certificates.html", count=num)


@app.route('/gallery/<num>')
def gallery(num):
    return render_template("gallery.html", count=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
