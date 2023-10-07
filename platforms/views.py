""" API endpoints for AppVerse.platforms """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.platforms.models import Platform
from appverse.platforms.serializers import PlatformSerializer


# Create your views here.
class PlatformViewSet(ModelViewSet):
    """PlatformViewSet: Create, view, update and delete Platforms"""

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["name"]
