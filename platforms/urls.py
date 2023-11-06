""" URLConf for AppVerse.platforms """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import PlatformAppsViewSet
from appverse.platforms.views import PlatformViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("platforms", PlatformViewSet, "platform")

sub_router = DefaultRouter()
sub_router.register("apps", PlatformAppsViewSet, "app")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "platforms/<int:id>/",
        include((sub_router.urls, "platforms"), namespace="platforms"),
    ),
]
