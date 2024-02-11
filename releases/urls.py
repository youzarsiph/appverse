""" URLConf for appverse.releases """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.releases.views import ReleaseViewSet
from appverse.reports.views import AppReportsViewSet
from appverse.reviews.views import AppReviewsViewSet
from appverse.screenshots.views import AppScreenshotsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=True)
router.register("releases", ReleaseViewSet, "release")

sub_router = DefaultRouter()
sub_router.register("screenshots", AppScreenshotsViewSet, "screenshot")
sub_router.register("reports", AppReportsViewSet, "report")
sub_router.register("reviews", AppReviewsViewSet, "review")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "releases/<int:id>/",
        include((sub_router.urls, "releases"), namespace="releases"),
    ),
]
