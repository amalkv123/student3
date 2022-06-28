import email
from unicodedata import name
from django.db import models

# Create your models here.

class student_details(models.Model):
    student_name=models.CharField(max_length=255)
    email=models.EmailField()
    gender=models.CharField(max_length=255)
    qulification=models.CharField(max_length=255)
    age=models.IntegerField()
    phone_number=models.CharField(max_length=255)
    date=models.DateField()
    address=models.CharField(max_length=255)

