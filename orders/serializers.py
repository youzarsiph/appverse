""" Serializers for appverse.orders """

from rest_framework.serializers import ModelSerializer
from appverse.orders.models import Order


# Create your serializers here.
class OrderSerializer(ModelSerializer):
    """Order serializer"""

    class Meta:
        """Meta data"""

        model = Order
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "user", "app", "ordered_at", "updated_at"]
