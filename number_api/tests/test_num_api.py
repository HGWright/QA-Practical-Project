from unittest.mock import patch
from flask_testing import TestCase
import requests_mock
from flask import url_for

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNum_API(TestBase):
    def test_numapi(self):
        with patch('random.randint') as r:
            r.return_value = '19'
            response = self.client.get(url_for('get_number'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'19', response.data)