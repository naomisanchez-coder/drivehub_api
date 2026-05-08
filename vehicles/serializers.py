from rest_framework import serializers
from .models import Owner, Vehicle

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'year', 'owner', 'owner_name']