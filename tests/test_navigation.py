# tests/test_navigation.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class NavigationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_navigation(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_attendance_navigation(self):
        response = self.client.get('/studentmgt/')
        self.assertEqual(response.status_code, 200)