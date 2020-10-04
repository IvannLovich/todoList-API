from django.test import TestCase
from django.test import Client
from .models import User

client = Client()

class UserEndpointTestCase(TestCase):

    def test_user_endpoint(self):
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
