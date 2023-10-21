""" API endpoints for AppVerse.apps """


from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from appverse.permissions import IsAppObjectOwner, IsAppOwner, IsDeveloper
from appverse.apps import models
from appverse.apps import serializers


# Create your views here.
class AppViewSet(ModelViewSet):
    """Create, view, update and delete Apps"""

    queryset = models.App.objects.all()
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "released_at", "updated_at"]
    filterset_fields = ["name", "platforms__name", "tags__name", "categories__name"]

    @action(methods=["get", "post"], detail=True)
    def approve(self, request, pk):
        """Approve Apps"""

        if not request.user.is_staff:
            return Response({"message": "Only admins can approve apps"})

        app = models.App.objects.get(pk=pk)
        message: str = f"App {app.name} "

        if app.approved:
            message += "disapproved"
            app.approved = False
        else:
            message += "approved"
            app.approved = True

        app.save()

        return Response({"message": message})

    @action(methods=["post"], detail=True)
    def install(self, request, pk):
        """Install the app"""

        app = models.App.objects.get(pk=pk)
        install, _ = models.Install.objects.get_or_create(
            app=app,
            user=request.user,
        )
        install.count += 1
        install.save()

        return Response({"message": f"Installing {app.name} app."})

    @action(methods=["post"], detail=True)
    def pre_order(self, request, pk):
        """Pre-order the app"""

        app = models.App.objects.get(pk=pk)
        order, _ = models.PreOrder.objects.get_or_create(
            app=app,
            user=request.user,
        )
        order.save()

        return Response({"message": f"Pre-ordering {app.name} app."})

    def retrieve(self, request, *args, **kwargs):
        """Create a view"""

        view, _ = models.View.objects.get_or_create(
            app=self.get_object(),
            user=request.user,
        )
        view.count += 1
        view.save()

        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        """Filter queryset by approved"""

        return super().get_queryset().filter(approved=True)

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


class PlatformAppViewSet(ModelViewSet):
    """Platform apps"""

    queryset = models.PlatformApp.objects.all()
    serializer_class = serializers.PlatformAppSerializer
    permission_classes = [IsAuthenticated, IsDeveloper, IsAppObjectOwner]
    search_fields = ["app__name", "platform__name"]
    ordering_fields = ["app__name", "platform__name", "released_at", "updated_at"]
    filterset_fields = ["app__name", "platforms__name"]


class ScreenshotViewSet(ModelViewSet):
    """Create, view, update and delete Screenshots"""

    queryset = models.Screenshot.objects.all()
    serializer_class = serializers.ScreenshotSerializer
    permission_classes = [IsAuthenticated, IsDeveloper, IsAppObjectOwner]
