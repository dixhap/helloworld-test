import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        tester = app.test_client(self)
        response = tester.post('/hello', json={'num': 101})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['description'], 'high')

        response = tester.post('/hello', json={'num': 99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['description'], 'low')

if __name__ == '__main__':
    unittest.main()