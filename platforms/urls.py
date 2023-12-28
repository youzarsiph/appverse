""" URLConf for appverse.platforms """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.platforms import views
from appverse.apps.views import PlatformAppsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("platforms", views.PlatformViewSet, "platform")
router.register("versions", views.PlatformViewSet, "version")

sub_router = DefaultRouter()
sub_router.register("apps", PlatformAppsViewSet, "app")
sub_router.register("versions", views.PlatformVersionsViewSet, "version")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "platforms/<int:id>/",
        include((sub_router.urls, "platforms"), namespace="platforms"),
    ),
]
