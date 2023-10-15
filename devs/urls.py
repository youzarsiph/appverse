""" URLConf for AppVerse.devs """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.devs.views import DeveloperViewSet


# Create your patterns here.
router = DefaultRouter()
router.register("developers", DeveloperViewSet, "developer")


urlpatterns = [
    path("", include(router.urls)),
]
