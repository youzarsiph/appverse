""" Serializers for appverse.tags """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.tags.models import Tag


# Create your serializers here.
class TagSerializer(HyperlinkedModelSerializer):
    """Tag serializer"""

    class Meta:
        """Meta data"""

        model = Tag
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
