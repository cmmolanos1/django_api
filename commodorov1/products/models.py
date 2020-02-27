from django.db import models
from places.models import Farm 


class Coffee(models.Model):
	""" Model where we input coffee specifications """
	farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_coffee')
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.IntegerField()
	variety = models.CharField(max_length=50)
	processing = models.CharField(max_length=50)
	crop_year = models.IntegerField()
	couping_score = models.IntegerField()