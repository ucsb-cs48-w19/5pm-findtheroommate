# Unit Tests file

import pytest
from app.models import User,Post

@pytest.fixture(scope='module')
def new_user():
    user = User(username = 'Test',email = 'test@ucsb.edu', password_hash = 'OurAppIsAwesome')
    return user

def test_new_user(new_user):
    """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, authenticated, and role fields are defined correctly
        """
    assert new_user.username == 'Test'
    assert new_user.email == 'test@ucsb.edu'
    assert new_user.password_hash == 'OurAppIsAwesome'
    assert not new_user.confirmed

@pytest.fixture(scope='module')
def new_post():
    post = Post(name = 'Test',body = 'Just for test.', email = 'test@ucsb.edu',gender = 'Female')
    return post

def test_new_post(new_post):
    assert (new_post.body == 'Just for test.')
    assert (new_post.email == 'test@ucsb.edu')
    assert (new_post.gender == 'Female')
    assert (new_post.name == 'Test')
