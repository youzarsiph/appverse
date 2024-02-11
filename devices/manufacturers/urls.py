""" URLConf for appverse.devices.manufacturers """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.devices.manufacturers import views


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("manufacturers", views.ManufacturerViewSet, "manufacturer")
router.register("models", views.DeviceModelViewSet, "model")

sub_router = DefaultRouter(trailing_slash=False)
sub_router.register("models", views.ManufacturerModelsViewSet, "model")

urlpatterns = [
    path("", include(router.urls)),
]
