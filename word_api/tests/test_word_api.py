from unittest.mock import patch
from flask_testing import TestCase
import requests_mock
from flask import url_for

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestWord_API(TestBase):
    def test_wordapi(self):
        with patch('random.choice') as r:
            r.return_value = 'Swing'
            response = self.client.get(url_for('get_word'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Swing', response.data)