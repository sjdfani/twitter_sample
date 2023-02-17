from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from users.models import User
from faker import Faker
from .models import Twittes


class TestSetUp(APITestCase):

    def setUp(self) -> None:
        fake = Faker()
        self.sign_up_url = reverse('users:sign_up_user')
        self.sign_in_url = reverse('users:sign_in_user')
        self.create_twittes_url = reverse('twittes:create_twittes')
        self.list_twittes_url = reverse('twittes:twittes_list')
        self.create_like_url = reverse('twittes:create_like')
        self.create_comment_url = reverse('twittes:create_comment')
        self.create_reTwittes_url = reverse('twittes:create_reTwittes')
        self.user_data = {
            'email': fake.email(),
            'username': fake.email().split('@')[0],
            'password': '123456'
        }
        self.twittes_data = {
            'message': fake.text(),
        }
        self.like_data = {
            'twittes': fake.unique.random_int(min=2, max=99),
        }
        self.comment_data = {
            'twittes': fake.unique.random_int(min=2, max=99),
            'message': fake.text()
        }
        self.re_twittes_data = {
            'twittes': fake.unique.random_int(min=2, max=99),
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class TestViews(TestSetUp):
    def test_cannot_create_twittes(self):
        response = self.client.post(
            self.create_twittes_url, self.twittes_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_create_twittes_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(
            self.create_twittes_url, self.twittes_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_like_correctly_unAuthorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        response = self.client.post(self.create_like_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_create_like_correctly_authorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_like_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_like_correctly_not_found(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_like_url, self.like_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_like_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        client.post(self.create_twittes_url, self.twittes_data)
        self.like_data['twittes'] = Twittes.objects.first().id
        response = client.post(self.create_like_url, self.like_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = client.post(self.create_like_url, self.like_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_comment_correctly_unAuthorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        response = self.client.post(self.create_comment_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_create_comment_correctly_authorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_comment_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_comment_correctly_not_found(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_comment_url, self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_comment_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        client.post(self.create_twittes_url, self.twittes_data)
        self.comment_data['twittes'] = Twittes.objects.first().id
        response = client.post(self.create_comment_url, self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_reTwittes_correctly_unAuthorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        response = self.client.post(self.create_reTwittes_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_create_reTwittes_correctly_authorized(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_reTwittes_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_reTwittes_correctly_not_found(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        response = client.post(self.create_reTwittes_url, self.re_twittes_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_reTwittes_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user)
        client.post(self.create_twittes_url, self.twittes_data)
        self.re_twittes_data['twittes'] = Twittes.objects.first().id
        response = client.post(self.create_reTwittes_url, self.re_twittes_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = client.post(self.create_reTwittes_url, self.re_twittes_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
