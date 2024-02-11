""" API endpoints for appverse.devices.manufacturers """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse.devices.manufacturers.models import Manufacturer, Model
from appverse.devices.manufacturers.serializers import (
    ManufacturerSerializer,
    ModelSerializer,
)


# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    """Create, view, update and delete Manufacturers"""

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]


class DeviceModelViewSet(ModelViewSet):
    """Create, view, update and delete Device Models"""

    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["manufacturer", "platform", "name"]


class ManufacturerModelsViewSet(DeviceModelViewSet):
    """Device Models of a manufacturer"""

    def get_queryset(self):
        """Filter queryset b manufacturer"""

        manufacturer = Manufacturer.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(manufacturer=manufacturer)

    def perform_create(self, serializer):
        """Adds a model to a manufacturer"""

        manufacturer = Manufacturer.objects.get(pk=self.kwargs["id"])
        serializer.save(manufacturer=manufacturer)
