""" Serializers for AppVerse.reviews """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(HyperlinkedModelSerializer):
    """Review serializer"""

    class Meta:
        """Meta data"""

        model = Review
        fields = [
            "id",
            "url",
            "user",
            "app",
            "comment",
            "rating",
            "reviewed_at",
            "updated_at",
        ]
