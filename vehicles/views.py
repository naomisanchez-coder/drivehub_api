from rest_framework import viewsets, filters
from .models import Owner, Vehicle
from .serializers import OwnerSerializer, VehicleSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'license_number']

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand', 'model']