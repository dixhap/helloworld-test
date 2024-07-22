import unittest
from app import app

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_evaluate_high(self):
        response = self.app.post('/evaluate', json={'value': 150})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['value'], 'high')

    def test_evaluate_low(self):
        response = self.app.post('/evaluate', json={'value': 50})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['value'], 'low')
    
    def test_evaluate_invalid_input(self):
        response = self.app.post('/evaluate', json={'value': 'invalid'})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid input')

    def test_evaluate_no_value(self):
        response = self.app.post('/evaluate', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid input')

if __name__ == '__main__':
    unittest.main()
