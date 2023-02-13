from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.sign_up_url = reverse('users:sign_up_user')
        self.sign_in_url = reverse('users:sign_in_user')
        self.user_data = {
            'username': 'test',
            'password': '123456'
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class TestViews(TestSetUp):

    def test_user_cannot_sign_up_correctly(self):
        response = self.client.post(self.sign_up_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_sign_up_correctly(self):
        response = self.client.post(
            self.sign_up_url, self.user_data, format='json')
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_sign_in_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user_data = {
            'username': self.user_data['username'],
            'password': '12345678',
        }
        response = self.client.post(
            self.sign_in_url, user_data, format='json'
        )
        self.assertEqual(response.status_code, 401)

    def test_user_can_sign_in_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        response = self.client.post(
            self.sign_in_url, self.user_data, format='json'
        )
        self.assertEqual(response.status_code, 200)
