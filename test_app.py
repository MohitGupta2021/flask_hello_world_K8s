import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World! I can make change at route: /change')

    def test_change(self):
        response = self.app.get('/change/1/25')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'quarters': 5}])

if __name__ == '__main__':
    unittest.main()
