from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class DayOfWeek(models.Model):
    DAYS_OF_WEEK = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    day = models.IntegerField(choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.DAYS_OF_WEEK[self.day][1]


class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=50, default="No Name")
    last_name = models.CharField(max_length=50, default="No Name")
    email_address = models.EmailField(max_length=254, default="none@forgot.com")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=50, default="No Name")
    last_name = models.CharField(max_length=50, default="No Name")
    email_address = models.EmailField(max_length=254, default="none@forgot.com")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Level(models.Model):
    name = models.CharField(max_length=50, default="Enter Name")

    def __str__(self):
        return self.name


class ClassGroup(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True
    )
    students = models.ManyToManyField(Student, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    day_of_week = models.ForeignKey(
        DayOfWeek, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.day_of_week.__str__() + " " + self.level.__str__()


class ClassSession(models.Model):
    class_group = models.ForeignKey(
        ClassGroup, on_delete=models.CASCADE, null=True, blank=True
    )
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        # Format the date (e.g., "Oct 05, 2023")
        date_str = self.date.strftime("%m/%d/%y") if self.date else "No Date"

        # Format the times (e.g., "07:00 PM")
        start_time_str = self.start_time.strftime("%I:%M %p") if self.start_time else "No Start Time"
        end_time_str = self.end_time.strftime("%I:%M %p") if self.end_time else "No End Time"

        # Return the formatted string
        return f"{date_str} {self.class_group} {start_time_str} - {end_time_str}"


class Attendance(models.Model):
    class_session = models.ForeignKey(ClassSession, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    is_present = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)