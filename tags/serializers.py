""" Serializers for AppVerse.tags """


from rest_framework.serializers import ModelSerializer
from appverse.tags.models import Tag


# Create your serializers here.
class TagSerializer(ModelSerializer):
    """Tag serializer"""

    class Meta:
        """Meta data"""

        model = Tag
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
