# regression_test.py
import requests

def test_regression_compare_number():
    response = requests.post('http://localhost:5000/compare', json={'number': 50})
    assert response.status_code == 200
    assert response.json == {'number': 50, 'result': 'low'}