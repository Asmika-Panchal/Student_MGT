# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse

from studentmgt.models import Student



class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_student_valid(self):
        response = self.client.post(reverse('add_student'), {
            'name': 'Amey',
            'email': 'amey@example.com',
            'course': 'IT',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.count(), 1)

    def test_student_list_view(self):
        Student.objects.create(name="Amey", email="a@a.com", course="CS")
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Amey")
