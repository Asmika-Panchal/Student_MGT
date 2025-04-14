from django.test import TestCase
from django.contrib.auth.models import User

class AuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='amey', password='pass123')

    def test_login_success(self):
        login = self.client.login(username='amey', password='pass123')
        self.assertTrue(login)

    def test_login_fail(self):
        login = self.client.login(username='amey', password='wrongpass')
        self.assertFalse(login)
