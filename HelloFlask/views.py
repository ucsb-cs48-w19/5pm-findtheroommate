from flask import Flask, render_template, request, url_for
from HelloFlask import app, db
from datetime import datetime
from HelloFlask.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required #for logout #for protection of login  
from HelloFlask.models import User
from werkzeug.urls import url_parse #for next redirect


@app.route('/')
@app.route('/home')
@login_required #Prectation for home page
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X") # bad code!! # strong 加粗

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("home.html", title='Home Page', posts=posts)


@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')

@app.route('/posts')
def posts():
    return render_template(
        "posts.html",
        detail = {'basic' : 'Currently, just a blank page'},
        title = "Posts",
        content = "Posts page for Flask.")

@app.route('/detail')
def detail():
    posts = [
              {'author': {'username': 'John'}, 
              'body': 'Beautiful day in Portland!'}, 
              {'author': {'username': 'Susan'},
              'body': 'The Avengers movie was so cool!'}
            ] 
    return render_template(
        "detail.html",
         title = "Details",
         content = "Details of this program.",
         posts = posts)
         

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  #first reprent the only result returned by query (match the name)
        if user is None or not user.check_password(form.password.data): #check the correctness of the assword
            flash('Invalid username or password') #error message
            return redirect(url_for('login'))  #redirect back
        login_user(user, remember=form.remember_me.data) #mark as current user in tuture operation
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/home') #currently can't type url_for('home'), don't know why


@app.route('/register', methods=['GET', 'POST']) #register page
def register():
    if current_user.is_authenticated: #If login, redirct to home page
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)