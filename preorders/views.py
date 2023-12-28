""" API endpoints for appverse.preorders """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.apps.models import App
from appverse.permissions import IsOwner
from appverse.preorders.models import PreOrder
from appverse.preorders.serializers import PreOrderSerializer


# Create your views here.
class PreOrderViewSet(ModelViewSet):
    """Create, view, update and delete Views"""

    queryset = PreOrder.objects.all()
    serializer_class = PreOrderSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserPreOrdersViewSet(PreOrderViewSet):
    """Pre orders of an app"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, app=app)

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
