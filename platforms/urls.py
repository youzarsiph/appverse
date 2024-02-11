""" URLConf for appverse.platforms """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import PlatformAppsViewSet
from appverse.platforms.views import PlatformViewSet
from appverse.platforms.versions.views import PlatformVersionsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("platforms", PlatformViewSet, "platform")
router.register("versions", PlatformViewSet, "version")

sub_router = DefaultRouter()
sub_router.register("apps", PlatformAppsViewSet, "app")
sub_router.register("versions", PlatformVersionsViewSet, "version")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "platforms/<int:id>/",
        include((sub_router.urls, "platforms"), namespace="platforms"),
    ),
]
