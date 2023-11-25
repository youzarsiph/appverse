""" API endpoints for AppVerse """


from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from appverse.permissions import IsAccountOwner
from appverse.serializers import UserSerializer


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """User ViewSet"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "delete"]:
            self.permission_classes = [IsAuthenticated, IsAccountOwner]

        return super().get_permissions()
