""" API endpoints for appverse.developers """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.developers.models import Developer
from appverse.developers.serializers import DeveloperSerializer


# Create your views here.
class DeveloperViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Developer profiles"""

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve developer profile"""

        developer = self.get_object()
        developer.is_approved = not developer.is_approved
        developer.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                "details": f"Developer {developer.name} is {'approved' if developer.is_approved else 'disapproved'}"
            },
        )

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve", "list"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()
