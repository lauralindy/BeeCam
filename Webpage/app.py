from firebase import firebase
from flask import Flask
from flask import render_template
#from .forms import firePut

app = Flask(__name__)
#firebase = firebase.FirebaseApplication("<path tofirebase app>", None)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name="Homepage")

@app.route('/testing')
def testing():
    return "index.html"

if __name__ == "__main__":
    app.run(debug=True)