""" Serializers for appverse.platforms """

from rest_framework.serializers import ModelSerializer
from appverse.platforms.models import Platform


# Create your serializers here.
class PlatformSerializer(ModelSerializer):
    """Platform serializer"""

    class Meta:
        """Meta data"""

        model = Platform
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
