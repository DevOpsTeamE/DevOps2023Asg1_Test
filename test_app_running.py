import pytest
from main import create_app 

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client

@pytest.fixture
def client(app):
    return app.test_client()


def test_starting_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Website' in response.data
    assert b'<button>Login</button>' in response.data
    assert b'<button>Register</button>' in response.data
