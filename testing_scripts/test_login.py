

def test_login_successfully(client):
    response = client.post('/login', json={'username': 'correctName', 'password': 'correctPW'})
    assert response.status_code == 200
    assert b'{"message": "Login Successful"}' in response.data

def test_login_unsuccessful(client):
    response = client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_password'})    
    assert response.status_code == 401
    assert b'{"message": "Invalid username or password"}' in response.data