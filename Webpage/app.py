from firebase import firebase
from flask import Flask, render_template, flash, request, redirect, url_for, session
from forms import FirePut

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://127.0.0.1:5000/', None)

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

@app.route('/mybees')
def mybees():
    return render_template("mybees.html")

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/imglink')
def imglink():
    return render_template("imglink.html")

@app.route('/testing')
def testing():
    return "index.html"

@app.route('/tryit')
def tryit():
    return render_template("try.html")

if __name__ == "__main__":
    app.run(debug=True)
    count = 0
    @app.route('/api/put', methods=['GET', 'POST'])
    def fireput():
        form = FirePut()
        if form.validate_on_submit():
            global count
            count += 1
            putData = {'Title' : form.title.data, 'Year' : form.year.data, 'Rating' : form.rating.data}
            firebase.put('/films', 'film' + str(count), putData)
            return render_template('api-put-result.html', form=form, putData=putData)
        return render_template('My-Form.html')