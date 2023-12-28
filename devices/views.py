""" API endpoints for appverse.devices """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse.permissions import IsOwner, IsReadOnly
from appverse.devices import models
from appverse.devices import serializers


# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    """Create, view, update and delete Manufacturers"""

    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]


class DeviceModelViewSet(ModelViewSet):
    """Create, view, update and delete Device Models"""

    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["manufacturer", "platform", "name"]


class ManufacturerModelsViewSet(DeviceModelViewSet):
    """Device Models of a manufacturer"""

    def get_queryset(self):
        """Filter queryset b manufacturer"""

        manufacturer = models.Manufacturer.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(manufacturer=manufacturer)

    def perform_create(self, serializer):
        """Adds a model to a manufacturer"""

        manufacturer = models.Manufacturer.objects.get(pk=self.kwargs["id"])
        serializer.save(manufacturer=manufacturer)


class DeviceViewSet(ModelViewSet):
    """Create, view, update and delete Devices"""

    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsReadOnly]
    search_fields = ["model__name", "model__manufacturer__name"]
    ordering_fields = ["id", "created_at", "updated_at"]
    filterset_fields = ["user", "model"]


class UserDevicesViewSet(DeviceViewSet):
    """Devices of a user"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by a user"""

        return super().get_queryset().filter(user=self.request.user)
