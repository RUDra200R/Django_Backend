from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Contact(models.Model):
#     username= models.CharField(max_length=15, null=True)
#     email = models.EmailField(max_length=50, unique=True)
#     phone = models.IntegerField(null=True, blank=True)
#     organname = models.CharField(max_length=15 , null=True, blank=True)
#     password = models.CharField(max_length=200, null=True)
#     message = models.TextField()


class Admin(AbstractUser):
    # user_ID = models.AutoField(primary_key=True, editable=False)
    # first_name = models.CharField(max_length=15, null=True)
    # last_name = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=200, null=True)
    message = models.TextField()
    phone= models.CharField(max_length=10, blank=True, null=True, unique=True)
    organization_Name = models.CharField(max_length=255, blank=True, null=True)