""" API endpoints for AppVerse.reports """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.apps.models import App
from appverse.reports.models import Report
from appverse.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["user__username", "app__name", "comment"]
    ordering_fields = ["reported_at", "updated_at"]
    filterset_fields = ["user", "app"]

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


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
