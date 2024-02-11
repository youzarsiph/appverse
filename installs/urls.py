""" URLConf for appverse.installs """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.installs.views import UserInstallsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("installs", UserInstallsViewSet, "install")


urlpatterns = [
    path("", include(router.urls)),
]
