from rest_framework import serializers
from .models import House

class HouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
        