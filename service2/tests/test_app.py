from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimal(TestBase):
    def test_get_animal(self):
        animal_list=[b"Cat",b"Chicken",b"Dog"]
        response = self.client.get(url_for('get_animal'))
        self.assertIn(response.data, animal_list)

    def test_post_animal_cat(self):
        response = self.client.post(
                url_for('post_animal'),
                data="Cat",
                follow_redirects=True)
        self.assertIn(response.data, b"Meow")

    def test_post_animal_dog(self):
        response = self.client.post(
                url_for('post_animal'),
                data="Dog",
                follow_redirects=True)
        self.assertIn(response.data, b"Bark")

    def test_post_animal_chicken(self):
        response = self.client.post(
                url_for('post_animal'),
                data="Chicken",
                follow_redirects=True)
        self.assertIn(response.data, b"Cluck")
