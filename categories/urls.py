""" URLConf for AppVerse.categories """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.categories.views import CategoryViewSet


# Create your patterns here.
router = DefaultRouter()
router.register("categories", CategoryViewSet, "category")


urlpatterns = [
    path("", include(router.urls)),
]
