""" URLConf for AppVerse.apps """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps import views


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("apps", views.AppViewSet, "app")
router.register("screenshots", views.ScreenshotViewSet, "screenshot")
router.register("permissions", views.PermissionViewSet, "permission")


urlpatterns = [
    path("apps/", include(router.urls)),
]
