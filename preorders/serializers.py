""" Serializers for AppVerse.preorders """


from rest_framework.serializers import ModelSerializer
from appverse.preorders.models import PreOrder


# Create your serializers here.
class PreOrderSerializer(ModelSerializer):
    """PreOrder serializer"""

    class Meta:
        """Meta data"""

        model = PreOrder
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "user", "app", "ordered_at", "updated_at"]
