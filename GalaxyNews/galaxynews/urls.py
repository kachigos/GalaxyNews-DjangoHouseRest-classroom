from django.contrib import admin
from django.urls import path
from news.views import NewsViewSet
from rest_framework.routers import SimpleRouter




router = SimpleRouter()
router.register(r'news', NewsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls