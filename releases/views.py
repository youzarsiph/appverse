""" API endpoints for appverse.releases """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse import permissions
from appverse.apps.models import App
from appverse.releases.models import Release
from appverse.releases.serializers import ReleaseSerializer


# Create your views here.
class ReleaseViewSet(ModelViewSet):
    """Create, list, retrieve, update and delete App Releases"""

    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.IsDeveloper,
        permissions.IsAppObjectOwner,
    ]
    search_fields = ["app__name", "platform__name"]
    ordering_fields = ["id", "app__name", "platform__name", "released_at", "updated_at"]
    filterset_fields = ["app", "platform"]


class AppReleasesViewSet(ReleaseViewSet):
    """App Releases for a platform"""

    def perform_create(self, serializer):
        """Add the app before save"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)
