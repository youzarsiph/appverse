""" API endpoints for appverse.reports """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.releases.models import Release
from appverse.reports.models import Report
from appverse.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["user__username", "release__app__name", "comment"]
    ordering_fields = ["id", "reported_at", "updated_at"]
    filterset_fields = ["user", "release__app"]

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

        release = Release.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(release=release)

    def perform_create(self, serializer):
        """Save report with app and user"""

        release = Release.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, release=release)
