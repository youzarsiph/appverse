""" URLConf for appverse.screenshots """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.screenshots.views import ScreenshotView, ScreenshotViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("screenshots", ScreenshotViewSet, "screenshot")


urlpatterns = [
    path("", include(router.urls)),
    path("screenshots/<int:pk>/image/", ScreenshotView.as_view()),
]
