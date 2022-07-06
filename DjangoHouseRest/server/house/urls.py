from django.urls import path
from .views import HouseCreateView

urlpatterns = [
    path('house/create/', HouseCreateView.as_view())
]