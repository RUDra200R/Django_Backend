from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    username= models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(null=True, blank=True)
    organname = models.CharField(max_length=15 , null=True, blank=True)
    password = models.CharField(max_length=200, null=True)
    message = models.TextField()
