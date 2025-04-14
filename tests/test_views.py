# tests/test_views.py
from django.urls import reverse
from studentmgt.models import Student
from coursemgt.models import Course
from datetime import date
from django.test import TestCase
from django.test import Client

class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(name="IT")

    def test_add_student_valid(self):
        response = self.client.post(reverse('add_student'), {
            'fname': 'Amey',
            'lname': 'Gaikwad',
            'dob': '2000-01-01',
            'gender': 'M',
            'st_email': 'amey@example.com',
            'pr_email': 'parent@example.com',
            'phone': '1234567890',
            'pr_phone': '0987654321',
            'address': 'Mumbai',
            'batch_mon': 'June',
            'batch_year': 2023,
            'courses': [self.course.id],  # For ManyToMany
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.count(), 1)

