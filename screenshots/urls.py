""" URLConf for AppVerse.screenshots """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.screenshots.views import ScreenshotViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("screenshots", ScreenshotViewSet, "screenshot")


urlpatterns = [
    path("", include(router.urls)),
]
