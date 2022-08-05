from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    esal=models.FloatField()
    eprofile=models.CharField(max_length=40)

    def __str__(self):
        return self.ename

class testapp_user(models.Model):
    real_name=models.CharField(max_length=40)
    user=models.OneToOneField(User, on_delete=models.CASCADE)