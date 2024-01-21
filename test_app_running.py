import pytest
from main import create_app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

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
    button_text = "Login"
    loginButton = response.find_element(By.XPATH, f'//button[text()="{button_text}"]') #Find button with text containing "Login"
    loginButton.click() #Click Login Button
    response.implicitly_wait(5) #Wait for 5 seconds
    current_page = response.current_url.split("/")[-1] #Get the name of the html file that user is redirected to after clicking the login button
    assert current_page == "login.html" 
    #assert response.status_code == 200
    #assert b'Welcome to My Website' in response.data
    #assert b'<button>Login</button>' in response.data
    #assert b'<button>Register</button>' in response.data
