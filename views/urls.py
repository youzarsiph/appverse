""" URLConf for appverse.views """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.views.views import UserViewsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("views", UserViewsViewSet, "view")


urlpatterns = [
    path("", include(router.urls)),
]
