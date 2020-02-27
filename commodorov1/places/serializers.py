from django.contrib.auth.models import User
from products.models import Coffee
from .models import Farm, Picture
from users.models import Profile
from rest_framework import serializers, fields


class ProfileSerializer(serializers.ModelSerializer):
	""" Serialization of the profile, for a future
	User serialization """
	class Meta:
		model = Profile
		fields = (
			'id',
			'user',
			'image'
			)

class UserSerializer(serializers.ModelSerializer):
	""" Serialization of the User, calling just
	some fields, and nesting the Profile serialization """
	profile_user = ProfileSerializer(read_only=True)

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'first_name',
			'last_name',
			'email',
			'profile_user'
			)

class CoffeeSerializer(serializers.ModelSerializer):
	""" Serialize the coffee, for a future farm
	serialization """
	class Meta:
		model = Coffee
		fields = (
			'id',
			'farm',
			'name',
			'description',
			'price',
			'variety',
			'processing',
			'crop_year',
			'couping_score'
			) 

class PictureSerializer(serializers.ModelSerializer):
	""" Serialize the list of pictures """
	class Meta:
		model = Picture
		fields = (
			'id',
			'farm',
			'image'
			)

class FarmSerializer(serializers.ModelSerializer):
	""" Farm serialisation, nesting all important fields
	to the json """
	farm_coffee = CoffeeSerializer(many=True)
	farm_picture = PictureSerializer(many=True)
	class Meta:
		model = Farm
		fields = (
			'id',
			'farm_name',
			'description',
			'region',
			'country',
			'farmer',
			'farm_coffee',
			'farm_picture'
			)
		