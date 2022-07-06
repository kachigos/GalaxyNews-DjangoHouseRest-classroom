from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer
from .models import News


# Create your views here.

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer