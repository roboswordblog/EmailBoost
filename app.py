from flask import Flask, render_template, request
from datamanagement import *
from ai import *

app = Flask(__name__)

loggedinUser = None
loggedinGmail = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['POST'])
def signup():
    return render_template('singup.html')


@app.route('/homelogin', methods=['POST'])
def homelogin():
    global loggedinUser
    username = request.form['username']
    password = request.form['password']
    loggedinUser = username
    if not getUser(username):
        return render_template('login.html', wrong=True)
    if getUser(username)[1] == password:
        return render_template('home.html', new='')
    else:
        return render_template('login.html', wrong=True)


@app.route('/homesignup', methods=['POST'])
def homesignup():
    global loggedinUser
    username = request.form['username']
    password = request.form['password']
    gmail = request.form['email']
    loggedinUser = username
    if addUser(username, password, gmail):
        return render_template('singup.html', error=True)
    return render_template('home.html', new='', cookad=True)


@app.route("/logout", methods=['POST', "GET"])
def logout():
    global loggedinUser, loggedinGmail
    loggedinUser = None
    loggedinGmail = None
    return render_template('index.html')


@app.route("/dashboard", methods=['POST'])
def dashboard():
    return render_template('home.html', new='', cookad=True)


@app.route("/pricing", methods=['POST'])
def pricing():
    return render_template('pricing.html', tier="Pro")


@app.route("/enhance", methods=['POST'])
def update():
    a = improve(request.form['body'])
    return render_template("home.html", new=a)


@app.route("/subscribe", methods=['POST'])
def subscribe():
    plan = request.form['plan']
    upgradeUser(loggedinUser, plan)
    return render_template("pricing.html", tier=plan)


app.run(debug=True)
