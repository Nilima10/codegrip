from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class ManagerProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True)
    company = models.CharField(max_length=50, null=True)

class EmployeeProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField(max_length=100, null=True)
    dob = models.DateField(null=True)
    company = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=20, null=True)