# Generated by Django 4.2.5 on 2023-11-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_remove_classgroup_day_of_week_classgroup_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='classgroup',
            name='name',
            field=models.CharField(default='Enter Name', max_length=50),
        ),
    ]
