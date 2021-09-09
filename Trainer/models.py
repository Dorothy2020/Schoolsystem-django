from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=16,null=True)
    email=models.EmailField(max_length=30,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    profession=models.CharField(max_length=20,null=True)
  
    contract=models.FileField(null=True)
    image=models.ImageField(upload_to="image/" , null=True)
    
    GENDER_CHOICES=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)

    biography=models.TextField(null=True)

    

