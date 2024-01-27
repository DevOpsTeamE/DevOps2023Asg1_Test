import pytest
from main import create_app 
from controllers.utilities.user import has_user, \
    get_user, \
    register_user
from mysql.connector.errors import IntegrityError

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_has_user():
    assert has_user('test_user')

def test_get_user():
    users =get_user('test_user', '')
    assert len(users) ==1
    user =users[0]
    assert user.password =='' and \
        user.username =='test_user' and \
        user.role_id == 0 and \
        user.is_active ==1

def test_register_successfully(client):
    register_user('test_user_1', 'password')
    assert has_user('test_user_1')
    users =get_user('test_user_1', 'password')
    user =users[0]
    assert user.username =='test_user_1'
    assert user.password == 'password'
    assert user.role_id == 1
    assert user.is_active ==0

def test_existing_registry(client):
    success =False
    try:
        register_user('test_user', 'password')
    except IntegrityError:
        success =True
    assert success
