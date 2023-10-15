""" URLConf for AppVerse """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appverse import views


# Create your patterns here.
router = DefaultRouter()

lc_map = {
    "get": "list",
    "post": "create",
}

rup_map = {
    "put": "update",
    "get": "retrieve",
    "delete": "destroy",
    "patch": "partial_update",
}

urlpatterns = [
    path("", include(router.urls)),
    # Apps
    path("", include("appverse.apps.urls")),
    # App Platforms
    path(
        "apps/<int:id>/platforms/",
        views.AppPlatformsViewSet.as_view(lc_map),
    ),
    path(
        "apps/<int:id>/platforms/<int:pk>/",
        views.AppPlatformsViewSet.as_view(rup_map),
    ),
    # App Screenshots
    path(
        "apps/<int:id>/screenshots/",
        views.AppScreenshotsViewSet.as_view(lc_map),
    ),
    path(
        "apps/<int:id>/screenshots/<int:pk>/",
        views.AppScreenshotsViewSet.as_view(rup_map),
    ),
    # App Reports
    path(
        "apps/<int:id>/reports/",
        views.AppReportsViewSet.as_view(lc_map),
    ),
    path(
        "apps/<int:id>/reports/<int:pk>/",
        views.AppReportsViewSet.as_view(rup_map),
    ),
    # App Reviews
    path(
        "apps/<int:id>/reviews/",
        views.AppReviewsViewSet.as_view(lc_map),
    ),
    path(
        "apps/<int:id>/reviews/<int:pk>/",
        views.AppReviewsViewSet.as_view(rup_map),
    ),
    # Developers
    path("", include("appverse.devs.urls")),
    path(
        "developers/<int:id>/apps/",
        views.DeveloperAppsViewSet.as_view({"get": "list"}),
    ),
    # Categories
    path("", include("appverse.categories.urls")),
    # Category Apps
    path(
        "categories/<int:id>/apps/",
        views.CategoryAppsViewSet.as_view({"get": "list"}),
    ),
    # Permissions
    path("", include("appverse.perms.urls")),
    # Platforms
    path("", include("appverse.platforms.urls")),
    # Platform Apps
    path(
        "platforms/<int:id>/apps/",
        views.PlatformAppsViewSet.as_view({"get": "list"}),
    ),
    # Reports
    path("", include("appverse.reports.urls")),
    # Tags
    path("", include("appverse.tags.urls")),
    # Tag Apps
    path(
        "tags/<int:id>/apps/",
        views.TagAppsViewSet.as_view({"get": "list"}),
    ),
]
