""" URLConf for appverse.apps """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse.apps import views
from appverse.reports.views import AppReportsViewSet
from appverse.reviews.views import AppReviewsViewSet
from appverse.screenshots.views import AppScreenshotsViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=True)
router.register("apps", views.AppViewSet, "app")

sub_router = DefaultRouter()
sub_router.register("screenshots", AppScreenshotsViewSet, "screenshot")
sub_router.register("platforms", views.AppPlatformsViewSet, "platform")
sub_router.register("reports", AppReportsViewSet, "report")
sub_router.register("reviews", AppReviewsViewSet, "review")


urlpatterns = [
    path("", include(router.urls)),
    path("apps/<int:pk>/icon", views.AppIconView.as_view()),
    path("apps/<int:pk>/cover", views.AppCoverView.as_view()),
    path(
        "apps/<int:id>/",
        include((sub_router.urls, "apps"), namespace="apps"),
    ),
]
