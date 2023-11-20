# Generated by Django 4.2.5 on 2023-11-20 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0002_attendance_classgroup_classsession_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_address',
            field=models.EmailField(default='forgot@forgot.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='Forgot', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Names', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]