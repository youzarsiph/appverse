""" API endpoints for AppVerse.apps """


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse.apps import models
from appverse.apps import serializers
from appverse.categories.models import Category
from appverse.devs.models import Developer
from appverse.installs.models import Install
from appverse.permissions import IsAppObjectOwner, IsAppOwner, IsDeveloper
from appverse.platforms.models import Platform
from appverse.preorders.models import PreOrder
from appverse.tags.models import Tag
from appverse.views.models import View


# Create your views here.
class AppViewSet(ModelViewSet):
    """Create, view, update and delete Apps"""

    queryset = models.App.objects.all()
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "released_at", "updated_at"]
    filterset_fields = ["name", "platforms__name", "tags__name", "categories__name"]

    @action(methods=["post"], detail=True)
    def approve(self, request, pk):
        """Approve Apps"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve developer profiles"},
                status=status.HTTP_403_FORBIDDEN,
            )

        app = models.App.objects.get(pk=pk)
        message: str = f"App {app.name} "

        if app.is_approved:
            message += "disapproved"
            app.is_approved = False
        else:
            message += "approved"
            app.is_approved = True

        app.save()

        return Response({"details": message})

    @action(methods=["post"], detail=True)
    def install(self, request, pk):
        """Install the app"""

        app = models.App.objects.get(pk=pk)
        install, _ = Install.objects.get_or_create(
            app=app,
            user=request.user,
        )
        install.count += 1
        install.save()

        return Response({"details": f"Installing {app.name} app."})

    @action(methods=["post"], detail=True)
    def pre_order(self, request, pk):
        """Pre-order the app"""

        app = models.App.objects.get(pk=pk)
        order, _ = PreOrder.objects.get_or_create(
            app=app,
            user=request.user,
        )
        order.save()

        return Response({"details": f"Pre-ordering {app.name} app."})

    def retrieve(self, request, *args, **kwargs):
        """Create a view"""

        view, _ = View.objects.get_or_create(
            app=self.get_object(),
            user=request.user,
        )
        view.count += 1
        view.save()

        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        """Filter queryset by approved"""

        return super().get_queryset().filter(is_approved=True)

    def get_serializer_class(self):
        """Return a serializer class based on self.action"""

        if self.action in ["retrieve", "update", "partial_update"]:
            self.serializer_class = serializers.DetailedAppSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes += [IsDeveloper]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsDeveloper, IsAppOwner]
        elif self.action == "approve":
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()

    def perform_create(self, serializer):
        """Save the object with owner"""

        if self.request.user.developer is not None:
            serializer.save(developer=self.request.user.developer)
            return

        return super().perform_create(serializer)


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


class PlatformAppViewSet(ModelViewSet):
    """Platform apps"""

    queryset = models.PlatformApp.objects.all()
    serializer_class = serializers.PlatformAppSerializer
    permission_classes = [IsAuthenticated, IsDeveloper, IsAppObjectOwner]
    search_fields = ["app__name", "platform__name"]
    ordering_fields = ["app__name", "platform__name", "released_at", "updated_at"]
    filterset_fields = ["app__name", "platforms__name"]


class AppPlatformsViewSet(PlatformAppViewSet):
    """Platforms of an app"""

    def perform_create(self, serializer):
        """Add the app before save"""

        app = models.App.objects.get(pk=self.kwargs["id"])
        serializer.save(app=app)

    def get_queryset(self):
        """Filter queryset by app"""

        app = models.App.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(app=app)
