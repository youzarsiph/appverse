""" API endpoints for appverse.views """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.permissions import IsOwner
from appverse.views.models import View
from appverse.views.serializers import ViewSerializer


# Create your views here.
class ViewViewSet(ModelViewSet):
    """Create, view, update and delete Views"""

    queryset = View.objects.all()
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserViewsViewSet(ViewViewSet):
    """Recently viewed apps"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
