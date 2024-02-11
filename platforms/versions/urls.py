""" URLConf for appverse.platforms.versions """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.platforms.versions.views import VersionViewSet


# Create your patterns here.
router = DefaultRouter()
router.register("versions", VersionViewSet, "version")


urlpatterns = [
    path("", include(router.urls)),
]
