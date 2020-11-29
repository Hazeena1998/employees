from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    usertype = models.CharField(max_length=50)

class Employee(models.Model):
    us = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to='gallery')

