""" API endpoints for AppVerse.reports """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
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
    filterset_fields = ["user__username", "app__name"]

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()
