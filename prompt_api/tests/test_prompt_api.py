from unittest.mock import patch
from flask_testing import TestCase
import requests_mock
from flask import url_for

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrompt_API(TestBase):
    def test_promptapi_without(self):
            response = self.client.post(url_for('get_prompt'), json={"word":"Swing", "num": "5"})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'with no additional challenge', response.data)

    def test_promptapi_with(self):
        with patch('random.choice') as a:
            a.return_value = 'while standing on one leg'
            response = self.client.get(url_for('get_prompt'), json={"word":"Swing", "num": "19"})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'while standing on one leg', response.data)
