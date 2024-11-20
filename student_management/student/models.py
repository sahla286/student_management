from django.db import models

# Create your models here.

class Student(models.Model):
    admission_number=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()
    image=models.ImageField(upload_to='student_image')