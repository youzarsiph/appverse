""" API endpoints for appverse.platforms.versions """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.platforms.models import Platform
from appverse.platforms.versions.models import Version
from appverse.platforms.versions.serializers import VersionSerializer


# Create your views here.
class VersionViewSet(ModelViewSet):
    """Create, view, update and delete PlatformVersions"""

    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["version"]
    ordering_fields = ["id", "version", "created_at", "updated_at"]
    filterset_fields = ["platform", "version"]


class PlatformVersionsViewSet(VersionViewSet):
    """Versions of platform"""

    def get_queryset(self):
        """Filter queryset by platform"""

        platform = Platform.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(platform=platform)
