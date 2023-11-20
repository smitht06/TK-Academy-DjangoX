from django.contrib import admin

# Register your models here.
from .models import Teacher, Student, ClassGroup, ClassSession, Attendance, Level, DayOfWeek

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ClassGroup)
admin.site.register(ClassSession)
admin.site.register(Attendance)
admin.site.register(Level)
admin.site.register(DayOfWeek)

