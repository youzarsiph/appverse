""" URLConf for AppVerse """


from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("api/", include(router.urls)),
]
