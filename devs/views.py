""" API endpoints for AppVerse.devs """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.devs.models import Developer
from appverse.devs.serializers import DeveloperSerializer


# Create your views here.
class DeveloperViewSet(ModelViewSet):
    """DeveloperViewSet: Create, view, update and delete Developer profiles"""

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["name"]
