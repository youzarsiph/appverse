""" Serializers for AppVerse.categories """


from rest_framework.serializers import ModelSerializer
from appverse.categories.models import Category


# Create your serializers here.
class CategorySerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
