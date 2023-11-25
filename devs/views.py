""" API endpoints for AppVerse.devs """


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.devs.models import Developer
from appverse.devs.serializers import DeveloperSerializer


# Create your views here.
class DeveloperViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Developer profiles"""

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve developer profile"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve developer profiles"},
                status=status.HTTP_403_FORBIDDEN,
            )

        developer = Developer.objects.get(pk=pk)
        message: str = f"Developer {developer.name} "

        if developer.is_approved:
            message += "disapproved"
            developer.is_approved = False
        else:
            message += "approved"
            developer.is_approved = True

        developer.save()

        return Response({"details": message})

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve", "list"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()
