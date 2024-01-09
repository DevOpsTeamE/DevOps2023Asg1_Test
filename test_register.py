import pytest
from main import create_app 

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


def test_register_successfully(client):
    response = client.post('/register', json={'username': 'newUser', 'password': 'newPassword'})
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_existing_registry(client):
    response = client.post('/register', json={'username': 'correctName', 'password': 'newPassword'})
    assert response.status_code == 400
    assert b'Username already exists. Please choose another username.' in response.data