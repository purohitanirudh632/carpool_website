import email
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Driver(models.Model):
    dn = models.CharField(max_length=10,  primary_key=True, verbose_name="Driver numer")
    name = models.CharField(max_length=30,verbose_name="Driver name",blank=True)
    contact = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length=20)  
    source = models.TextField() 
    destination = models.TextField()

    class Meta:
        verbose_name = "Driver"
    
    def __str__(self):
        return f"driver-{self.dn}"
    

class Userprof(models.Model):
      name = models.CharField(max_length=30,verbose_name="User name",blank=True)
      contact = models.CharField(max_length = 20)
      email = models.EmailField()
      password = models.CharField(max_length=20)  
      class Meta:
         verbose_name = "Userprof"
    
      def __str__(self):
         return f"Userprof-{self.name}"