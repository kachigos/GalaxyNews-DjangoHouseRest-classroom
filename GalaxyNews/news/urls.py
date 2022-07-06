from django.urls import path
from .views import NewsViewSet
from rest_framework.routers import SimpleRouter
from galaxynews.urls import urlpatterns


router = SimpleRouter()
router.register(r'news', NewsViewSet)

urlpatterns += router

