import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from app import app  # Hilangkan "src."


class TestGreetingApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Masukkan Nama Anda', response.data)  # Cek apakah halaman utama tampil

    def test_greet_post(self):
        response = self.app.post('/', data={'name': 'Miko'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Miko!', response.data)  # Cek apakah sapaan muncul

if __name__ == '__main__':
    unittest.main()
