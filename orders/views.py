""" API endpoints for appverse.orders """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.apps.models import App
from appverse.permissions import IsOwner
from appverse.orders.models import Order
from appverse.orders.serializers import OrderSerializer


# Create your views here.
class OrderViewSet(ModelViewSet):
    """Create, view, update and delete Views"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserOrdersViewSet(OrderViewSet):
    """Pre orders of an app"""

    def perform_create(self, serializer):
        """Add a screenshot to an app"""

        app = App.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, app=app)

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
