""" API endpoints for AppVerse.reports """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.reports.models import Report
from appverse.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(ModelViewSet):
    """ReportViewSet: Create, view, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "app__name", "comment"]
    ordering_fields = ["reported_at", "updated_at"]
    filterset_fields = ["user__username", "app__name"]
