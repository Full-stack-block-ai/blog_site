from flask import render_template, flash, redirect,url_for,request
from urllib.parse import urlsplit
from app import app
from app.forms import LoginForm,RegistrationForm
import sqlalchemy as sa
from flask_login import current_user,login_user, logout_user,login_required
from app import db
from app.models import User

# Serves homepage for '/' and '/index'
@app.route('/')
@app.route('/index')
@login_required
def index():

    
    posts = [
        {
        'author':{'username': 'john'},
        'body': 'Rainy day in the uk'
    },
    {
        'author':{'username': 'alice'},
        'body': 'Early start at work!'
    }]

    return render_template('index.html', title = 'home' , posts=posts)

# Handles login page and form submission
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

#logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')