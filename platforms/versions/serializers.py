""" Serializers for appverse.platforms.versions """

from rest_framework.serializers import ModelSerializer
from appverse.platforms.versions.models import Version


# Create your serializers here.
class VersionSerializer(ModelSerializer):
    """Version serializer"""

    class Meta:
        """Meta data"""

        model = Version
        read_only_fields = ["platform"]
        fields = ["id", "platform", "version", "created_at", "updated_at"]
