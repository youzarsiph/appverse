""" URLConf for AppVerse.apps """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from appverse.apps.views import AppViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("apps/", include(router.urls)),
]
