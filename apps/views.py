""" API endpoints for AppVerse.apps """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.apps import serializers
from appverse.apps.models import App, Permission, Screenshot


# Create your views here.
class AppViewSet(ModelViewSet):
    """AppViewSet: Create, view, update and delete Apps"""

    queryset = App.objects.all()
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = []
    filterset_fields = []

    def get_queryset(self):
        """Filter queryset by approved"""

        if self.request.user.is_staff:
            return super().get_queryset()

        return super().get_queryset().filter(approved=True)


class ScreenshotViewSet(ModelViewSet):
    """ScreenshotViewSet: Create, view, update and delete Screenshots"""

    queryset = Screenshot.objects.all()
    serializer_class = serializers.ScreenshotSerializer
    permission_classes = [IsAuthenticated]


class PermissionViewSet(ModelViewSet):
    """PermissionViewSet: Create, view, update and delete Permissions"""

    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name", "description"]
    ordering_fields = []
    filterset_fields = []
