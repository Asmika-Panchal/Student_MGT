from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class NavigationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create users for different roles
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass', email='admin@test.com')
        self.staff_user = User.objects.create_user(username='staff', password='staffpass', email='staff@test.com')
        self.student_user = User.objects.create_user(username='student', password='studentpass', email='student@test.com')

    def test_homepage_navigation(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/admin_home/')  # Adjust URL if different
        self.assertEqual(response.status_code, 200)

    def test_staff_dashboard(self):
        self.client.login(username='staff', password='staffpass')
        response = self.client.get('/staff_home/')  # Adjust if needed
        self.assertIn(response.status_code, [200, 302])  # 302 if redirected to login or dashboard

    def test_student_dashboard(self):
        self.client.login(username='student', password='studentpass')
        response = self.client.get('/student_home/')  # Adjust if needed
        self.assertIn(response.status_code, [200, 302])

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/admin_home/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
