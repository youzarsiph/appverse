""" URLConf for appverse.devices """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.devices import views


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("manufacturers", views.ManufacturerViewSet, "manufacturer")
router.register("models", views.DeviceModelViewSet, "model")
router.register("devices", views.DeviceViewSet, "device")

sub_router = DefaultRouter(trailing_slash=False)
sub_router.register("models", views.ManufacturerModelsViewSet, "model")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "manufacturers/<int:id>/",
        include((sub_router.urls, "devices"), namespace="devices"),
    ),
]
