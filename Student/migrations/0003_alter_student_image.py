# Generated by Django 3.2.5 on 2021-08-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='documents/'),
        ),
    ]