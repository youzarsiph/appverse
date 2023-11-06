""" URLConf for AppVerse.categories """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps.views import CategoryAppsViewSet
from appverse.categories.views import CategoryViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("categories", CategoryViewSet, "category")

sub_router = DefaultRouter()
sub_router.register("apps", CategoryAppsViewSet, "app")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "categories/<int:id>/",
        include((sub_router.urls, "categories"), namespace="categories"),
    ),
]
