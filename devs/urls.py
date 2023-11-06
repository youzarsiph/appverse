""" URLConf for AppVerse.devs """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import DeveloperAppsViewSet
from appverse.devs.views import DeveloperViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("developers", DeveloperViewSet, "developer")

sub_router = DefaultRouter()
sub_router.register("apps", DeveloperAppsViewSet, "app")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "developers/<int:id>/",
        include((sub_router.urls, "developers"), namespace="developers"),
    ),
]
