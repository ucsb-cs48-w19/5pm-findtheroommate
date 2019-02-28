# Functional test file

import pytest
from app import *
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User(email = 'test@ucsb.edu', password_hash = 'OurAppIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app,db)
    testing_client = app.test_client()
    
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    
    yield testing_client  # this is where the testing happens!
    
    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
    
    # Insert user data
    user1 = User(email='test1@ucsb.edu', password_hash='test_1')
    user2 = User(email='test2@ucsb.edu', password_hash='test_2')
    db.session.add(user1)
    db.session.add(user2)
    
    # Commit the changes for the users
    db.session.commit()
    
    yield db  # this is where the testing happens!
    
    db.drop_all()

def test_home_page(test_client):
    """
        GIVEN a Flask application
        WHEN the '/' page is requested (GET)
        THEN check the response is valid
        """
    response = test_client.get('/')
    assert response.status_code == 200
#    assert b"Welcome to the Flask User Management Example!" in response.data
#    assert b"Need an account?" in response.data
#    assert b"Existing user?" in response.data

