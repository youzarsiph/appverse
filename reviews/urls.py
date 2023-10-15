""" URLConf for AppVerse.reviews """


from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your patterns here.
router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
]
