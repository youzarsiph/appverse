""" URLConf for AppVerse """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.view import UserViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, "user")


urlpatterns = [
    path("", include(router.urls)),
    # Apps
    path("", include("appverse.apps.urls")),
    # Categories
    path("", include("appverse.categories.urls")),
    # Developers
    path("", include("appverse.developers.urls")),
    # Devices
    path("", include("appverse.devices.urls")),
    # Installs
    path("", include("appverse.installs.urls")),
    # Orders
    path("", include("appverse.orders.urls")),
    # Permissions
    path("", include("appverse.perms.urls")),
    # Platforms
    path("", include("appverse.platforms.urls")),
    # Platform Versions
    path("", include("appverse.platforms.versions.urls")),
    # Releases
    path("", include("appverse.releases.urls")),
    # Reports
    path("", include("appverse.reports.urls")),
    # Reviews
    path("", include("appverse.reviews.urls")),
    # Screenshots
    path("", include("appverse.screenshots.urls")),
    # Tags
    path("", include("appverse.tags.urls")),
    # Views
    path("", include("appverse.views.urls")),
]
