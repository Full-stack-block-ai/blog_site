from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    user = {"username": "Lucy"}
    posts = [
        {
        'author':{'username': 'john'},
        'body': 'Rainy day in the uk'
    },
    {
        'author':{'username': 'alice'},
        'body': 'Early start at work!'
    }]

    return render_template('index.html', title = 'home' ,user = user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In',form=form)

