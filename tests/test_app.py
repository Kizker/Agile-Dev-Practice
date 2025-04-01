import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from app import app  # Hilangkan "src."


class TestGreetingApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_greet_default(self):
        response = self.app.get('/greet')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, User!', response.data)

    def test_greet_name(self):
        response = self.app.get('/greet?name=Miko')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Miko!', response.data)

if __name__ == '__main__':
    unittest.main()