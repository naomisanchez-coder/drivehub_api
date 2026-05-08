from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, VehicleViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]