from firebase import firebase
from flask import Flask, render_template, flash, request, redirect, url_for, session
#from .forms import firePut

app = Flask(__name__)
#firebase = firebase.FirebaseApplication("<path tofirebase app>", None)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/service')
def service():
    return render_template("index.html")

@app.route('/process')
def process():
    return render_template("index.html#tf-process")

@app.route('/about')
def about():
    return render_template("index.html#tf-about")

@app.route('/ack')
def ack():
    return render_template("index.html#tf-acknowledgements")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/testing')
def testing():
    return "index.html"

if __name__ == "__main__":
    app.run(debug=True)