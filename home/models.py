from django.db import models

# Create your models here.
class Home(models.Model):
    username=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    cgpa=models.CharField(max_length=10)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)