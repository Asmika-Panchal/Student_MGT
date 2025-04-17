# tests/test_models.py
from datetime import date
from studentmgt.models import Student
from coursemgt.models import Course
from django.test import TestCase

class StudentModelTest(TestCase):
    def setUp(self):
        # Corrected the way Course is created based on the updated model
        self.course = Course.objects.create(c_id="C101", cname="IT", cduration=3)

    def test_create_student(self):
        student = Student.objects.create(
            fname="Amey",
            lname="Gaikwad",
            dob=date(2000, 1, 1),
            gender="M",
            st_email="amey@test.com",
            pr_email="parent@test.com",
            phone="1234567890",
            pr_phone="0987654321",
            address="Mumbai",
            batch_mon="June",
            batch_year=2023
        )
        student.courses.set([self.course])  # Correctly linking the course
        self.assertEqual(student.fname, "Amey")
        self.assertEqual(student.courses.count(), 1)
