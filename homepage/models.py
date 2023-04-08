from django.db import models


# Create your models here.
class Place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pic=models.ImageField(upload_to='pics',default='pics/default_place.png')
    place_region=models.CharField(max_length=50,null=True,blank=True)
    place_name=models.CharField(max_length=50)
    state_name=models.CharField(max_length=50)
    place_desc=models.TextField()
    place_alias=models.TextField()
    related_pics=models.FileField(upload_to='relatedpics',default='null')

class hotel(models.Model):
    location=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    offer=models.BooleanField(default=False)
    price=models.IntegerField()
    address=models.CharField(max_length=50)