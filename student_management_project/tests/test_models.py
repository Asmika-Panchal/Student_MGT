from django.test import TestCase
from student_app.models import Student

class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(name="Amey", email="amey@test.com", course="IT")
        self.assertEqual(student.name, "Amey")
        self.assertEqual(student.email, "amey@test.com")
        self.assertEqual(student.course, "IT")

    def test_duplicate_email_not_allowed(self):
        Student.objects.create(name="A", email="same@test.com", course="CS")
        with self.assertRaises(Exception):
            Student.objects.create(name="B", email="same@test.com", course="IT")
