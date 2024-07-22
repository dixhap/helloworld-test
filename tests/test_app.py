# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_compare_number_high(client):
    response = client.post('/compare', json={'number': 101})
    assert response.status_code == 200
    assert response.json == {'number': 101, 'result': 'high'}

def test_compare_number_low(client):
    response = client.post('/compare', json={'number': 99})
    assert response.status_code == 200
    assert response.json == {'number': 99, 'result': 'low'}

def test_compare_number_invalid_input(client):
    response = client.post('/compare', json={'number': 'abc'})
    assert response.status_code == 400