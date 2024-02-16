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


def test_starting_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the TSAO Capstone Records System' in response.data
    assert b'Sign In' in response.data
