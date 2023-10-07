""" URLConf for AppVerse.tags """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from appverse.tags.views import TagViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("tags/", include(router.urls)),
]
