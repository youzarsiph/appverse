""" URLConf for AppVerse.apps """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps import views


# Create your patterns here.
router = DefaultRouter()
router.register("apps", views.AppViewSet, "app")


urlpatterns = [
    path("", include(router.urls)),
]
