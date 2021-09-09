from django.shortcuts import render
from Student.models import Student
from Trainer .models import Trainer
from Course.models import Course
from cal .models import Event

def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    cal=Event.objects.count()
    data={"students":students,"trainers":trainers,"courses":courses,"cals":cal}
    return render(request,"home.html",data)