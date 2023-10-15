""" URLConf for AppVerse.platforms """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.platforms.views import PlatformViewSet


# Create your patterns here.
router = DefaultRouter()
router.register("platforms", PlatformViewSet, "platform")


urlpatterns = [
    path("", include(router.urls)),
]
