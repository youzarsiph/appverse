""" Serializers for AppVerse.devs """


from rest_framework.serializers import ModelSerializer
from appverse.devs.models import Developer


# Create your serializers here.
class DeveloperSerializer(ModelSerializer):
    """Developer serializer"""

    class Meta:
        """Meta data"""

        model = Developer
        fields = [
            "id",
            "url",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]
