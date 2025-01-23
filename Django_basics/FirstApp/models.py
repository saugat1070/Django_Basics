from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Employee(models.Model):
    id_no = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.FloatField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class StudentInfo(models.Model):
    id_no = models.IntegerField()
    name = models.CharField(max_length=30)
    clss_no = models.IntegerField()
    Mark = models.FloatField()
    image = models.ImageField(null=True,upload_to='images/')

class PhotoFromExternal(models.Model):
    image = models.ImageField(null=True,upload_to='images/')

class form_submission(models.Model):
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    
    
class UserRegistration(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=20)
    password = models.CharField(validators=[MinLengthValidator(8),MaxLengthValidator])