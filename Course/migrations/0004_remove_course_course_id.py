# Generated by Django 3.2.6 on 2021-09-02 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20210831_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_id',
        ),
    ]
