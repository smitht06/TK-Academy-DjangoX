from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import (
    DayOfWeek,
    Teacher,
    Student,
    Level,
    ClassGroup,
    ClassSession,
    Attendance,
)
from django.utils import timezone

User = get_user_model()


class DayOfWeekTestCase(TestCase):
    def setUp(self):
        DayOfWeek.objects.create(day=0)  # Monday

    def test_day_of_week_str(self):
        monday = DayOfWeek.objects.get(day=0)
        self.assertEqual(str(monday), "Monday")


class TeacherTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="teacher1", email="teacher1@example.com")
        Teacher.objects.create(user=user, first_name="John", last_name="Doe")

    def test_teacher_str(self):
        teacher = Teacher.objects.get(first_name="John")
        self.assertEqual(str(teacher), "John Doe")


class StudentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="student1", email="student1@example.com")
        Student.objects.create(user=user, first_name="Jane", last_name="Doe")

    def test_student_str(self):
        student = Student.objects.get(first_name="Jane")
        self.assertEqual(str(student), "Jane Doe")


class LevelTestCase(TestCase):
    def setUp(self):
        Level.objects.create(name="Beginner")

    def test_level_str(self):
        level = Level.objects.get(name="Beginner")
        self.assertEqual(str(level), "Beginner")


class ClassGroupTestCase(TestCase):
    def setUp(self):
        teacher = Teacher.objects.create(first_name="John", last_name="Doe")
        level = Level.objects.create(name="Intermediate")
        day = DayOfWeek.objects.create(day=2)  # Wednesday
        ClassGroup.objects.create(teacher=teacher, level=level, day_of_week=day)

    def test_class_group_str(self):
        class_group = ClassGroup.objects.get(level__name="Intermediate")
        self.assertEqual(str(class_group), "Wednesday Intermediate")


class ClassSessionTestCase(TestCase):
    def setUp(self):
        class_group = ClassGroup.objects.create()
        ClassSession.objects.create(
            class_group=class_group,
            start_time=timezone.now(),
            end_time=timezone.now(),
            date=timezone.now().date(),
        )

    def test_class_session_str(self):
        session = ClassSession.objects.first()
        session_str = str(session)
        self.assertTrue(session.start_time.strftime("%I:%M %p") in session_str)
        self.assertTrue(session.end_time.strftime("%I:%M %p") in session_str)


class AttendanceTestCase(TestCase):
    def setUp(self):
        session = ClassSession.objects.create()
        student = Student.objects.create(first_name="Jane", last_name="Doe")
        Attendance.objects.create(
            class_session=session, student=student, is_present=True
        )

    def test_attendance_is_present(self):
        attendance = Attendance.objects.first()
        self.assertTrue(attendance.is_present)
