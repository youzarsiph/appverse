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
    # Devices
    path("", include("appverse.devices.urls")),
    # Developers
    path("", include("appverse.devs.urls")),
    # Installs
    path("", include("appverse.installs.urls")),
    # Permissions
    path("", include("appverse.perms.urls")),
    # Platforms
    path("", include("appverse.platforms.urls")),
    # POrders
    path("", include("appverse.orders.urls")),
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
