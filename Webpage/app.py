from firebase import firebase
from flask import Flask, render_template, flash, request, redirect, url_for, session
from forms import FirePut
import database


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

@app.route('/hive1')
def hive1():
    return render_template("hive1.html")

@app.route('/hive2')
def hive2():
    return render_template("hive2.html")

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/imglink')
def imglink():
    paths = database.findCells("/Users/EmmaXu/Documents/Programming/ABeeCam/Big Pic/image.jpg")
    paths1 = paths[0:6]
    paths2=paths[6:12]
    paths3=paths[12:18]
    paths4=paths[18:24]
    paths5=paths[24:30]
    paths6=paths[30:36]
    paths7=paths[36:42]
    paths8=paths[42:48]
    paths9=paths[48:54]
    paths10=paths[54:60]
    paths11=paths[60:66]
    paths12=paths[66:72]
    paths13=paths[72:78]
    #paths14=paths[78:84]
    #paths15=paths[84:90]
    #paths16=paths[90]
    return render_template("imglink.html", paths1=paths1, paths2=paths2, paths3=paths3, paths4=paths4, paths5=paths5, paths6=paths6, paths7=paths7, paths8=paths8, paths9=paths9, path10=paths10, paths11=paths11, paths12=paths12, paths13=paths13)

@app.route('/imglink2')
def imglink2():
    paths = database.findCells("/Users/EmmaXu/Documents/Programming/ABeeCam/Big Pic/iRED.jpg")
    paths1 = paths[0:6]
    paths2=paths[6:12]
    paths3=paths[12:18]
    paths4=paths[18:24]
    paths5=paths[24:30]
    paths6=paths[30:36]
    paths7=paths[36:42]
    paths8=paths[42:47]
    return render_template("imglink2.html", paths1=paths1, paths2=paths2, paths3=paths3, paths4=paths4, paths5=paths5, paths6=paths6, paths7=paths7, paths8=paths8)


@app.route('/testing')
def testing():
    return "index.html"

@app.route('/show')
def show():
    return render_template("show.html")

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
