""" API endpoints for AppVerse """


from appverse.apps.models import App
from appverse.apps.views import AppViewSet, PlatformAppViewSet, ScreenshotViewSet
from appverse.categories.models import Category
from appverse.devs.models import Developer
from appverse.platforms.models import Platform
from appverse.reports.views import ReportViewSet
from appverse.reviews.views import ReviewViewSet
from appverse.tags.models import Tag


# Create your views here.
class AppPlatformsViewSet(PlatformAppViewSet):
    """Platforms of an app"""

    def perform_create(self, serializer):
        """Add the app before save"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)


class AppScreenshotsViewSet(ScreenshotViewSet):
    """Screenshots of an app"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)


class AppReportsViewSet(ReportViewSet):
    """Reports of an app"""

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)

    def perform_create(self, serializer):
        """Save report with app and user"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, app=app)


class AppReviewsViewSet(ReviewViewSet):
    """Reviews of an app"""

    def get_queryset(self):
        """Filter queryset by app"""

        app = App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)

    def perform_create(self, serializer):
        """Save report with app and user"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, app=app)


class DeveloperAppsViewSet(AppViewSet):
    """Apps of a developer"""

    def get_queryset(self):
        """Filter queryset by developer"""

        developer = Developer.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(developer=developer)


class CategoryAppsViewSet(AppViewSet):
    """Apps of category"""

    def get_queryset(self):
        """Filter queryset by category"""

        category = Category.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(categories=category)


class PlatformAppsViewSet(AppViewSet):
    """Apps of a platform"""

    def get_queryset(self):
        """Filter queryset by platform"""

        platform = Platform.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(platforms=platform)


class TagAppsViewSet(AppViewSet):
    """Apps of a tag"""

    def get_queryset(self):
        """Filter queryset by tag"""

        tag = Tag.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(tags=tag)
