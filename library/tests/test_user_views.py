from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from library.models import User


class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse('create-user')
        data = {'name': 'John Doe', 'email': 'john@example.com',
                'membership_date': '2022-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_users(self):
        url = reverse('list-users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_by_id(self):
        user = User.objects.create(
            name='Test User', email='test@example.com', membership_date='2022-01-01')
        url = reverse('get-user-by-id', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
