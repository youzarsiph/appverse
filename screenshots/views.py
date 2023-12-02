""" API endpoints for AppVerse.screenshots """


from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.apps.models import App, PlatformApp
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

        return super().get_queryset().filter(app__developer=self.request.user.developer)


class AppScreenshotsViewSet(ScreenshotViewSet):
    """Screenshots of an app"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)


class PlatformAppScreenshotsViewSet(ScreenshotViewSet):
    """Screenshots of an app for a platform"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = App.objects.get(pk=self.kwargs["id"])
        platform = PlatformApp.objects.get(pk=self.kwargs["p_id"])
        serializer.save(app=app, platform_app=platform)

    def get_queryset(self):
        """Filter queryset by app and platform"""

        app = App.objects.get(pk=self.kwargs["id"])
        platform = PlatformApp.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app, platform_app=platform)


class ScreenshotView(DetailView):
    """Screenshots images"""

    model = Screenshot

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
