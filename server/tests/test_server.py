from unittest.mock import patch
from flask_testing import TestCase
import requests_mock
from flask import url_for

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://challenge_word_api:5003/get_word', json={"word":"Swing"})
            mocker.get('http://challenge_number_api:5001/get_number', json={"num": "5"})
            mocker.post('http://challenge_prompt_api:5002/get_prompt', json={'prompt':'with no additional challenge'})
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your challenge is to describe Swing in 5 words with no additional challenge', response.data)
