from flask import Flask
from flask import render_template

app = Flask(__name__)

#Home Page part
@app.route('/')
def main():
    return render_template('home_page.html')

#Sign Up Page part
@app.route('/signup')
def signUp():
    return 'Sign up page'


#Login page part
@app.route('/login')
def login():
    return 'Login Page'

#Personal profile part
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile page'.format(username)


