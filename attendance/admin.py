from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import (
    Teacher,
    Student,
    ClassGroup,
    ClassSession,
    Attendance,
    Level,
    DayOfWeek,
)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ClassGroup)
admin.site.register(ClassSession)
admin.site.register(Level)
admin.site.register(DayOfWeek)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "class_session", "is_present")
    list_filter = ("student", "class_session", "is_present")
    search_fields = ("student", "class_session", "is_present")


admin.site.register(Attendance, AttendanceAdmin)
