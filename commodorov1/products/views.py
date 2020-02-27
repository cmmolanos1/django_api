from django.shortcuts import render
from .models import Coffee
from rest_framework import generics
from places.serializers import *


class CoffeesListView(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class CoffeesView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoffeeSerializer
    queryset = Coffee.objects.all()
