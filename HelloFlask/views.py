from flask import Flask, render_template, request, url_for, flash, redirect
from HelloFlask import app, db
from datetime import datetime
from HelloFlask.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm, EditPostForm #Profile form, 每个在form创建的form都需要import
from flask_login import current_user, login_user, logout_user, login_required #for logout #for protection of login  
from HelloFlask.models import User, Post
from werkzeug.urls import url_parse #for next redirect
from HelloFlask.email import send_password_reset_email, send_email_confirmation_email


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

    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('home', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template("home.html", title='Home Page', posts=posts.items, next_url=next_url,
                           prev_url=prev_url) #paginate object is not iterable, but paginate.items can



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
        send_email_confirmation_email(user)
        flash('Congratulation, A confirmation email has been sent via email.') #改改？？
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>') #specific page for users: <username> indicates that the variable can change dynamicly with real input
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id)
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_posts/<username>/<id>', methods=['GET', 'POST'])
@login_required
def edit_posts(username,id):
    if(current_user.username != username):
        return redirect(url_for('home'))
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(id=id).first_or_404() #要括号！！！！！
    form = EditPostForm()
    if form.validate_on_submit():
        posts.name = form.name.data
        posts.email = form.email.data
        posts.gender = form.gender.data
        posts.body = form.body.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET': #Get 表示用户第一次使用，所以给空白form， 如果==Post 代表input出错（貌似/(ㄒoㄒ)/~~）
        form.name.data = posts.name
        form.email.data = posts.email
        form.gender.data = posts.gender
        form.body.data = posts.body
    return render_template('edit_posts.html', user=user, posts=posts, form=form)

@app.route('/delete_post/<username>/<id>', methods=['GET', 'POST'])
@login_required
def delete_post(username,id):
    if(current_user.username != username):
        return redirect(url_for('home'))
    target = Post.query.filter_by(id=id).first_or_404()
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('user', username=current_user.username))



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
    id = current_user.get_id() #ID是一样的
    user = User.query.get(id);
    if not user.confirmed:
        flash('Please confirm your email first!')
        return redirect(url_for('home'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, email=form.email.data, gender=form.gender.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('home'))

    return render_template('make_posts.html', title='Make your Post',
                           form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated: #Check log in
        return redirect(url_for('home'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/email_confirmation/<token>', methods=['GET', 'POST'])
@login_required
def email_confirmation(token):
    email = User.verify_email_confirmation_token(token)
    user = User.query.filter_by(email=email).first_or_404()
    if not user:
        return redirect(url_for('home'))
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
        return redirect(url_for('login'))
    return render_template('email_confirmation.html')