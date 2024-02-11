""" API endpoints for appverse.screenshots """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.releases.models import Release
from appverse.permissions import IsAppObjectOwner, IsDeveloper
from appverse.screenshots.models import Screenshot
from appverse.screenshots.serializers import ScreenshotSerializer


# Create your views here.
class ScreenshotViewSet(ModelViewSet):
    """Create, view, update and delete Screenshots"""

    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [IsAuthenticated, IsDeveloper, IsAppObjectOwner]

    def get_queryset(self):
        """Filter queryset by developer"""

        return (
            super()
            .get_queryset()
            .filter(release__app__developer=self.request.user.developer)
        )


class AppScreenshotsViewSet(ScreenshotViewSet):
    """Screenshots of an app"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = Release.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        release = Release.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(release=release)


class PlatformAppScreenshotsViewSet(ScreenshotViewSet):
    """Screenshots of an app for a platform"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        release = Release.objects.get(pk=self.kwargs["id"])
        serializer.save(release=release)

    def get_queryset(self):
        """Filter queryset by app and platform"""

        release = Release.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(release=release)
