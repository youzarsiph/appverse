""" URLConf for appverse.apps """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import AppViewSet
from appverse.releases.views import AppReleasesViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=True)
router.register("apps", AppViewSet, "app")

sub_router = DefaultRouter()
sub_router.register("platforms", AppReleasesViewSet, "platform")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "apps/<int:id>/",
        include((sub_router.urls, "apps"), namespace="apps"),
    ),
]
