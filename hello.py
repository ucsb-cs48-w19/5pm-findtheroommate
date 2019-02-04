import flask
import firebase_admin
from firebase_admin import db
from flask import render_template
from firebase_admin import credentials

app = flask.Flask(__name__)

firebase_admin.initialize_app({
    credential: admin.credentials.cert({
    "private_key": process.env.FIREBASE_PRIVATE_KEY,
    "client_email": process.env.FIREBASE_CLIENT_EMAIL,
  }),
  databaseURL:"https://findtheroommate.firebaseio.com"
});
HELLO = db.reference('hello')

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


@app.route('/test', methods=['POST'])
def create_user():
    req = flask.request.json
    user = HELLO.push(req)
    return (flask.jsonify({'id': user.key}), 201)

