from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    role=models.CharField(max_length=50)

# Create your models here.
