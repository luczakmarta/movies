import datetime
import random
from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/index')
def homepage2():
    movies = ["Titanic"]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)