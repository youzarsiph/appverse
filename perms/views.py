""" API endpoints for appverse.perms """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.perms.models import Permission
from appverse.perms.serializers import PermissionSerializer


# Create your views here.
class PermissionViewSet(ModelViewSet):
    """Create, view, update and delete Permissions"""

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["name", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]
