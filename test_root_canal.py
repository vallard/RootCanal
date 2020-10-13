import os
import pytest

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root_path(client):
    response = client.get('/')
    assert(response.status_code == 200)

def test_non_existing_path(client):
    response = client.get('/there/is/no file$@#4')
    assert(response.status_code == 400)

def test_get_file(client):
    response = client.get('/foo1')
    assert(response.status_code == 200)
    print(response)

def test_get_dir(client):
    response = client.get('/bar')
    assert(response.status_code == 200)
    js = response.get_json()
    assert('contents' in js)

def test_hidden(client):
    response = client.get('/.hidden')
    assert(response.status_code == 200)
    js = response.get_json()
    assert('contents' in js)
    assert(len(js['contents']) > 0)
