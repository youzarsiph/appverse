""" Serializers for AppVerse.platforms """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.platforms.models import Platform


# Create your serializers here.
class PlatformSerializer(HyperlinkedModelSerializer):
    """Platform serializer"""

    class Meta:
        """Meta data"""

        model = Platform
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
