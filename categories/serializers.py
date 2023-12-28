""" Serializers for appverse.categories """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.categories.models import Category


# Create your serializers here.
class CategorySerializer(HyperlinkedModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
