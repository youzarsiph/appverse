""" URLConf for appverse.perms """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.perms.views import PermissionViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("permissions", PermissionViewSet, "permission")


urlpatterns = [
    path("", include(router.urls)),
]
