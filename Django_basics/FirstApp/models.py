from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    
    
from django.contrib.auth.models import BaseUserManager

class UserRegistrationManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)
 
class UserRegistration(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=8,validators=[MaxLengthValidator(3),MaxLengthValidator(8)])
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserRegistrationManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    def __str__(self):
        return self.name
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True