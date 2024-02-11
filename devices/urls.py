""" URLConf for appverse.devices """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.devices.manufacturers.views import (
    ManufacturerViewSet,
    DeviceModelViewSet,
    ManufacturerModelsViewSet,
)


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("manufactures", ManufacturerViewSet, "manufacture")
router.register("models", DeviceModelViewSet, "model")

sub_router = DefaultRouter()
sub_router.register("models", ManufacturerModelsViewSet, "model")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "manufacturers/<int:id>/",
        include((sub_router.urls, "manufacturers"), namespace="manufacturers"),
    ),
]
