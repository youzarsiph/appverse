""" URLConf for AppVerse.categories """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.categories.views import CategoryViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("categories", CategoryViewSet, "category")


urlpatterns = [
    path("categories/", include(router.urls)),
]
