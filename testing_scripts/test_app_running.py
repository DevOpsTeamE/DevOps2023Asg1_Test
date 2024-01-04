
def test_starting_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Website' in response.data
    assert b'<button>Login</button>' in response.data
    assert b'<button>Register</button>' in response.data