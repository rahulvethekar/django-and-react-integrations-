from asyncio import FastChildWatcher
from email.policy import default
from django.db import models

# Create your models here.


class Student(models.Model):
    rn = models.IntegerField(primary_key = True,blank=False)
    name = models.CharField(max_length = 30)
    marks = models.IntegerField(default = 0)
    city = models.CharField(max_length = 30)


    
