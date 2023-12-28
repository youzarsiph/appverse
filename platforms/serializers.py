""" Serializers for appverse.platforms """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.platforms.models import Platform, Version


# Create your serializers here.
class PlatformSerializer(HyperlinkedModelSerializer):
    """Platform serializer"""

    class Meta:
        """Meta data"""

        model = Platform
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]


class VersionSerializer(HyperlinkedModelSerializer):
    """PlatformVersion serializer"""

    class Meta:
        """Meta data"""

        model = Version
        fields = ["id", "platform", "version", "created_at", "updated_at"]
