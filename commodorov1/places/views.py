from django.shortcuts import render
from .models import Farm, Picture
from rest_framework import generics
from .serializers import *


class FarmsListView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FarmsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()

class PicturesListView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PicturesView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()