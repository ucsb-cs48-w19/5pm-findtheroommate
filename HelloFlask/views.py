from flask import Flask, render_template, request, url_for
from HelloFlask import app, db
from datetime import datetime
from HelloFlask.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm #Profile form, 每个在form创建的form都需要import
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required #for logout #for protection of login  
from HelloFlask.models import User, Post
from werkzeug.urls import url_parse #for next redirect


@app.before_request #Function executates right after the call for view function
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()  #utcnow() -- UTC 时间
        db.session.commit()


@app.route('/')
@app.route('/home')
@login_required #Prectation for home page
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X") # bad code!! # strong 加粗

    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template("home.html", title='Home Page', posts=posts)



@app.route('/about_us')
def about_us():

    return render_template(
        "about_us.html",
         title = "About us",
         content = "Currently, under construction!!"
         )
         

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

@app.route('/user/<username>') #specific page for users: <username> indicates that the variable can change dynamicly with real input
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST']) #Editing profile page
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET': #Get 表示用户第一次使用，所以给空白form， 如果==Post 代表input出错（貌似/(ㄒoㄒ)/~~）
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/make_posts', methods=['GET', 'POST']) #Post page: just a test page
def make_posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, email=form.email.data, gender=form.gender.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('home'))

    return render_template('make_posts.html', title='Make your Post',
                           form=form)
