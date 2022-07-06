from django.shortcuts import render
from rest_framework import generics
from .serializers import HouseSerializers

class HouseCreateView(generics.CreateAPIView):
    serializer_class = HouseSerializers