""" API endpoints for appverse.devices """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse.permissions import IsOwner, IsReadOnly
from appverse.devices.models import Device
from appverse.devices.serializers import DeviceSerializer


# Create your views here.
class DeviceViewSet(ModelViewSet):
    """Create, view, update and delete Devices"""

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
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
