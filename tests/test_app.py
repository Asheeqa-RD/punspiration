import unittest
from app import create_app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_puns_by_category(self):
        response = self.client.get('/puns/animals')
        self.assertEqual(response.status_code, 200)
        
    def test_random(self):
        response=self.client.get('/puns/random')
        self.assertEqual(response.status_code, 200)
        
        
        
if __name__ == '__main__':
    unittest.main()
