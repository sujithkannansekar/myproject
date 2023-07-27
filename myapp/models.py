from django.db import models
import os

import datetime
from django.contrib.auth.models import User

# Create your models here.
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)

class Folvika(models.Model):
    name=models.CharField(max_length=25,default='')
    place=models.CharField(max_length=35,default='')
    price=models.CharField(max_length=35,default='')
    site_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.CharField(max_length=200,default='')

    def __str__(self):
     return self.name
    
class reserve(models.Model):
   country_choice=(("INDIA","india"),("SRILANKA","srilanka"))
   Hotelname=models.CharField(max_length=35,default='')
   Firstname=models.CharField(max_length=20,default='')
   Lastname=models.CharField(max_length=20,default='')
   Mail=models.EmailField(max_length=30,default='')
   Mobile=models.IntegerField(default='')
   Country=models.CharField(max_length=20,choices=country_choice,default='')
   Guest=models.IntegerField(default='')
   From_date=models.CharField(max_length=10,default='')
   To_date=models.CharField(max_length=10,default='')

 
class reserves(models.Model):
   country_choice=(("INDIA","india"),("SRILANKA","srilanka"))
   Hotelname=models.CharField(max_length=35,default='')
   Firstname=models.CharField(max_length=20,default='')
   Lastname=models.CharField(max_length=20,default='')
   Mail=models.EmailField(max_length=30,default='')
   Mobile=models.IntegerField(default='')
   Country=models.CharField(max_length=20,choices=country_choice,default='')
   Guest=models.IntegerField(default='')
   From_date=models.CharField(max_length=10,default='')
   To_date=models.CharField(max_length=10,default='')


