#testing server with pytest
from server import app

def test_server():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == 'Welcome to Digitpol'