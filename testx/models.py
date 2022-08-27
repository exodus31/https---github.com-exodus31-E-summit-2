from email.policy import default
from operator import mod
from pyexpat import model
from statistics import mode
from timeit import default_timer
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Enterp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100)
    bplan = models.CharField(max_length=1000, default="Not Shared Yet")
    qpitch = models.CharField(max_length=1000, default="Not Shared Yet")
    cfunds = models.CharField(max_length=1000, default="Not Shared Yet")
    rfunding = models.CharField(max_length=1000, default="Not Shared Yet")
    field = models.CharField(max_length=1000, default="General")
    is_investor = models.BooleanField(default=False)   
    image = models.ImageField(default='1920-1.jpg')

    def __str__(self):
        return self.name

class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    details = models.CharField(max_length=500,default="")
    networth = models.CharField(max_length=1000, default="Not Shared Yet")
    comphold = models.CharField(max_length=1000, default="Not Shared Yet")
    invfield = models.CharField(max_length=1000, default="General")   
    firmname = models.CharField(max_length=200, default="")
    image = models.ImageField(default='1920-1.jpg')
    is_investor = models.BooleanField(default=False)    

    def __str__(self):
        return self.name

class Forum(models.Model):      
    title = models.CharField(max_length=500)
    details = models.CharField(max_length=1000)
    posteruname = models.CharField(max_length=100)
    forfield = models.CharField(max_length=100, default="General")
    image = models.ImageField(default='1920-1.jpg')

    def __str__(self):
        return self.posteruname

class Comments(models.Model):
    senderuname = models.CharField(max_length=50,default='')
    recieveruname = models.CharField(max_length=50,default='')
    comment = models.CharField(max_length=2000,default='')    

    def __str__(self):
        return self.recieveruname
