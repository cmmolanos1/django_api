from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics
from places.serializers import *


class UsersListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
