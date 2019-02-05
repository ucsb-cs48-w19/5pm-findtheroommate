import flask
import firebase_admin
import os
import json
from firebase_admin import db
from flask import render_template
from firebase_admin import credentials

app = flask.Flask(__name__)

temp_credential = {}
temp_credential["type"] = str(os.environ.get("type"))
temp_credential["token_uri"] = str(os.environ.get("token_uri"))
temp_credential["project_id"] = str(os.environ.get("project_id"))
temp_credential["private_key_id"] = str(os.environ.get("private_key_id"))
temp_credential["client_x509_cert_url"] = str(os.environ.get("client_x509_cert_url"))
temp_credential["client_id"] = str(os.environ.get("client_id"))
temp_credential["client_email"] = str(os.environ.get("client_email"))
temp_credential["auth_uri"] = str(os.environ.get("auth_uri"))
temp_credential["auth_provider_x509_cert_url"] = str(os.environ.get("auth_provider_x509_cert_url"))
print(temp_credential)
temp_credential["private_key"] = str(os.environ.get("private_key"))
print(temp_credential)
with open('result.json', 'w') as fp:
    json.dump(temp_cresdential, fp)
j = json.dumps(d, indent=4)
f = open('result.json', 'r')
print(j,file = f)
cred = credentials.Certificate('result.json')

firebase_admin.initialize_app(cred,options={
    'databaseURL': "https://findtheroommate.firebaseio.com"
})

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

