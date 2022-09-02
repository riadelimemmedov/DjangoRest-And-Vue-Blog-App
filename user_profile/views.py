from django.shortcuts import render
from rest_framework import generics

from .serializers import *
from .models import *

# Create your views here.
#!ProfileListCreateView
class ProfileListCreateView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer