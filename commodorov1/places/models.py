from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
	""" Model where we save information about the farms, their 
	specifications and pictures """
	farm_name = models.CharField(max_length=50)
	owner_name = models.CharField(default="", max_length=200)
	description = models.TextField()
	region = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	farmer = models.ForeignKey(User, on_delete=models.CASCADE)

class Picture(models.Model):
	""" Model where we save the path to the diferent pictures
	of a farm """
	farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_picture')
	image = models.ImageField(default='default.jpg', upload_to='farm_pics')
