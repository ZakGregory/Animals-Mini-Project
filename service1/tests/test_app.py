from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_football(self):
        with patch('requests.get') as get:
            with patch('requests.post') as post:
                get.return_value.text = "Cat"
                post.return_value.text= "Meow"
                response = self.client.get(url_for('home'))
                self.assertIn(b'CatMeow', response.data)
