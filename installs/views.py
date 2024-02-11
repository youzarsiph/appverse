""" API endpoints for appverse.installs """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.permissions import IsOwner, IsReadOnly
from appverse.installs.models import Install
from appverse.installs.serializers import InstallSerializer


# Create your views here.
class InstallViewSet(ModelViewSet):
    """Create, view, update and delete Installs"""

    queryset = Install.objects.all()
    serializer_class = InstallSerializer
    permission_classes = [IsAuthenticated, IsOwner, IsReadOnly]


class UserInstallsViewSet(InstallViewSet):
    """Installed apps"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
