""" URLConf for AppVerse.tags """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.tags.views import TagViewSet


# Create your patterns here.
router = DefaultRouter()
router.register("tags", TagViewSet, "tag")


urlpatterns = [
    path("", include(router.urls)),
]
