from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=28,null=True)
    syllabus=models.PositiveSmallIntegerField(null=True)
    course_code=models.CharField(max_length=12,null=True)
    course_trainer=models.CharField(max_length=20,null=True,blank=True)
    course_duration=models.CharField(max_length=14,null=True)
    
    
   
   

   