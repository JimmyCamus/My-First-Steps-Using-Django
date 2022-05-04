import json
from django.test import TestCase
from rest_framework.test import APIClient

from .models import (
    Person,
    Pet
)


class PersonTests(TestCase):
    def setUp(self):
        # Create a dummy person model
        person_1 = Person(email='person_1@domain.com',
                       first_name='first_1',
                       last_name='last_1',
                       rut='000000001')
        person_1.save()

    def test_get_persons(self):
        client = APIClient()
        response = client.get('/api/petclub/persons/', format='json')
        self.assertEqual(json.loads(response.content), {
                         'data': [{'id': 1, 'email': 'person_1@domain.com', 'first_name': 'first_1', 'last_name': 'last_1', 'rut': '000000001'}]})

    def test_create_person(self):
        client = APIClient()
        response = client.post(
            '/api/petclub/persons/',
            {
                'email': 'test@domain.com',
                'first_name': 'test',
                'last_name': 'test',
                'rut': '111111111'
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': 2, 'email': 'test@domain.com', 'first_name': 'test', 'last_name': 'test', 'rut': '111111111'}})

    def test_update_person(self):
        client = APIClient()
        response = client.patch(
            '/api/petclub/persons/',
            {
                'id': 1,
                'email': 'person_1_edit@domain.com',
                'first_name': 'first_1_edit',
                'last_name': 'last_1',
                'rut': '000000001'
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': 1, 'email': 'person_1_edit@domain.com', 'first_name': 'first_1_edit', 'last_name': 'last_1', 'rut': '000000001'}})

    def test_delete_person(self):
        client = APIClient()
        response = client.delete(
            '/api/petclub/persons/',
            {
                'id': 1,
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': None, 'email': 'person_1@domain.com', 'first_name': 'first_1', 'last_name': 'last_1', 'rut': '000000001'}})


class PetTests(TestCase):
    def setUp(self):
        # Create a dummy pet model
        pet_1 = Pet(species='dog',
                    name='name',
                    age=1,
                    color='black')
        pet_1.save()

    def test_get_pet(self):
        client = APIClient()
        response = client.get('/api/petclub/pets/', format='json')
        self.assertEqual(json.loads(response.content), {
                         'data': [{'id': 1, 'species': 'dog', 'name': 'name', 'age': 1, 'color': 'black'}]})

    def test_create_pet(self):
        client = APIClient()
        response = client.post(
            '/api/petclub/pets/',
            {
                'species': 'dog',
                'name': 'test',
                'age': 2,
                'color': 'yellow'
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': 2, 'species': 'dog', 'name': 'test', 'age': 2, 'color': 'yellow'}})

    def test_update_pet(self):
        client = APIClient()
        response = client.patch(
            '/api/petclub/pets/',
            {
                'id': 1,
                'species': 'dog',
                'name': 'name_test',
                'age': 1,
                'color': 'black_test'
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': 1, 'species': 'dog', 'name': 'name_test', 'age': 1, 'color': 'black_test'}})

    def test_delete_pet(self):
        client = APIClient()
        response = client.delete(
            '/api/petclub/pets/',
            {
                'id': 1,
            }, format='json')
        self.assertEqual(
            json.loads(response.content), {
                'data': {'id': None, 'species': 'dog', 'name': 'name', 'age': 1, 'color': 'black'}})
