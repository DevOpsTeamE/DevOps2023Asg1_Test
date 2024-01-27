from test import client, app
from flask import session

def test_login_successfully(client):
    with client:
        response = client.post('/login', data={'username': 'test_user', 'password': ''}, follow_redirects=True)
        assert response.status_code == 200
        assert session.get('role_name') == 'Admin'
        assert session.get('user')['username'] == 'test_user'
        assert session.get('user')['password'] == ''
        assert len(response.history) == 1
        assert response.request.path == '/admin/'

def test_login_unsuccessful(client):
    response = client.post('/login', data={'username': 'wrong_user', 'password': 'password'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(response.history) == 0
    assert response.request.path == '/login'