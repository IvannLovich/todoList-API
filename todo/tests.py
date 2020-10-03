from django.test import TestCase
from django.test import Client
from .models import Folder

client = Client()

class EndpointsTestCase(TestCase):

    def test_folder_endpoint(self):
        response = client.get('/api/todo/folders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_task_endpoint(self):
        response = client.get('/api/todo/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')