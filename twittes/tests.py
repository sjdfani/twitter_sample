from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self) -> None:
        self.sign_up_url = reverse('users:sign_up_user')
        self.sign_in_url = reverse('users:sign_in_user')
        self.create_twittes_url = reverse('twittes:create_twittes')
        self.list_twittes_url = reverse('twittes:twittes_list')
        self.token_obtain_pair_url = reverse('token_obtain_pair')
        self.user_data = {
            'username': 'test',
            'password': '123456'
        }
        self.data = {
            'message': 'Hello',
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class TestViews(TestSetUp):
    def test_cannot_create_twittes(self):
        response = self.client.post(
            self.create_twittes_url, self.data, format='json'
        )
        self.assertEqual(response.status_code, 401)

    def test_can_create_twittes_correctly(self):
        self.client.post(self.sign_up_url, self.user_data, format='json')
        # response = self.client.post(
        #     self.sign_in_url, self.user_data, format='json'
        # )
        client = APIClient()
        res = client.post(self.token_obtain_pair_url,
                          self.user_data, format='json')
        token = res.data['token']
        client.credentials(HTTP_AUTHORIZATION='JWT' + token)
        res = client.post(self.create_twittes_url, self.data, format='json')
        # header = {
        #     'Authorization': f"Bearer {response.data['tokens']['access']}"
        # }
        # print(header)
        # response = self.client.post(
        #     self.create_twittes_url, self.data, headers=header, format='json'
        # )
        self.assertEqual(res.status_code, 200)
