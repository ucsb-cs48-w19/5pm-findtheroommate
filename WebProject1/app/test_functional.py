# Functional test file

import pytest, os
from app.models import User, Post
from app import app, db

@pytest.fixture(scope='module')
def new_user():
    user = User(email = 'test@ucsb.edu', password_hash = 'OurAppIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    db.drop_all()
    db.create_all()

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
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code, 200
    

def test_valid_login(test_client,init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(email='test1@ucsb.edu', password_hash='test_1'),follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


def test_valid_logout(test_client,init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(email='test2@ucsb.edu', password_hash='test_2'),follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    
