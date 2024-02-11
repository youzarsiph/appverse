""" API endpoints for appverse.apps """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse import permissions
from appverse.apps import serializers
from appverse.apps.models import App
from appverse.categories.models import Category
from appverse.developers.models import Developer
from appverse.installs.models import Install
from appverse.platforms.models import Platform
from appverse.orders.models import Order
from appverse.tags.models import Tag
from appverse.views.models import View


# Create your views here.
class AppViewSet(ModelViewSet):
    """Create, list, retrieve, update and destroy Apps"""

    queryset = App.objects.all()
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "released_at", "updated_at"]
    filterset_fields = ["name", "platforms", "tags", "categories"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve Apps"""

        app = self.get_object()
        app.is_approved = not app.is_approved
        app.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                "details": f"App {app.name} is {'approved' if app.is_approved else 'disapproved'}"
            },
        )

    @action(methods=["post"], detail=True)
    def install(self, request, pk):
        """Install the app"""

        app = self.get_object()
        install, _ = Install.objects.get_or_create(
            app=app,
            user=request.user,
        )
        install.count += 1
        install.save()

        return Response({"details": f"Installing {app.name} app."})

    @action(methods=["post"], detail=True)
    def order(self, request, pk):
        """Pre-order the app"""

        app = self.get_object()
        order, _ = Order.objects.get_or_create(
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

        if self.request.user.is_staff:
            return super().get_queryset()

        return super().get_queryset().filter(is_approved=True)

    def get_serializer_class(self):
        """Return a serializer class based on self.action"""

        if self.action == "retrieve":
            self.serializer_class = serializers.Depth1AppSerializer
        elif self.action in ["update", "partial_update"]:
            self.serializer_class = serializers.RetrievedAppSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes += [permissions.IsDeveloper]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [permissions.IsDeveloper, permissions.IsAppOwner]
        elif self.action == "approve":
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()

    def perform_create(self, serializer):
        """Save the object with owner"""

        serializer.save(developer=self.request.user.developer)


class DeveloperAppsViewSet(AppViewSet):
    """Apps of a developer"""

    permission_classes = [IsAuthenticated, permissions.IsReadOnly]

    def get_queryset(self):
        """Filter queryset by developer"""

        developer = Developer.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(developer=developer)


class CategoryAppsViewSet(AppViewSet):
    """Apps of category"""

    permission_classes = [IsAuthenticated, permissions.IsReadOnly]

    def get_queryset(self):
        """Filter queryset by category"""

        category = Category.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(categories=category)


class PlatformAppsViewSet(AppViewSet):
    """Apps of a platform"""

    def get_queryset(self):
        """Filter queryset by platform"""

        platform = Platform.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(platforms__platform=platform)


class TagAppsViewSet(AppViewSet):
    """Apps of a tag"""

    permission_classes = [IsAuthenticated, permissions.IsReadOnly]

    def get_queryset(self):
        """Filter queryset by tag"""

        tag = Tag.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(tags=tag)
