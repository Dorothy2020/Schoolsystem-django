from django.db import models

# Create your models here.


class Student(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=16,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    email=models.EmailField(max_length=30,null=True)
    # phone_number=models.CharField(max_length=15,null=True)
    student_id=models.CharField(max_length=12,null=True)
    student_class=models.CharField(max_length=10,null=True,blank=True)
    parent_name=models.CharField(max_length=14)
    parent_phone=models.CharField(max_length=13)
    passport=models.CharField(max_length=15,null=True,blank=True)
    mentor=models.CharField(max_length=20,null=True)
    room_number=models.CharField(max_length=3,null=True,blank=True)
    laptop_number=models.CharField(max_length=10,null=True,blank=True)
    big_sister =models.CharField(max_length=15,null=True)
    # nationality=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="image/" , null=True)

    COUNTRY_CHOICES=(
        (u'K','Kenya'),
        (u'U','Uganda'),
        (u'R','Rwanda')
    )
    nationality=models.CharField(max_length=20,choices=COUNTRY_CHOICES,null=True)
    GENDER_CHOICES=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others')
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)

    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    