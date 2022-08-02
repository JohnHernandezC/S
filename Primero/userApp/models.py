from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuarios (AbstractUser):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    telefono=models.CharField(max_length=15, blank=False )
    correo=models.CharField(max_length=255, blank=False, null=False , unique=True) 
    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=['username']
    
    
    


