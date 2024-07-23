import unittest
from app import app

class TestAppRegression(unittest.TestCase):
    def assert_response(self, response, expected_value, expected_description):
        self.assertEqual(response.status_code, 200)
        json_response = response.json  # Get the json response as a dictionary
        self.assertEqual(json_response['value'], expected_value)
        self.assertEqual(json_response['description'], expected_description)

    def test_hello_world_regression(self):
        tester = app.test_client(self)
        self.assert_response(tester.post('/hello', json={'num': 101}), 101, 'high')
        self.assert_response(tester.post('/hello', json={'num': 99}), 99, 'low')

if __name__ == '__main__':
    unittest.main()