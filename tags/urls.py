""" URLConf for appverse.tags """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import TagAppsViewSet
from appverse.tags.views import TagViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("tags", TagViewSet, "tag")

sub_router = DefaultRouter()
sub_router.register("apps", TagAppsViewSet, "app")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "tags/<int:id>/",
        include((sub_router.urls, "tags"), namespace="tags"),
    ),
]
