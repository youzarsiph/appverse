""" Serializers for AppVerse.reviews """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(HyperlinkedModelSerializer):
    """Review serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = ["app", "user"]
        fields = [
            "id",
            "url",
            "app",
            "user",
            "comment",
            "rating",
            "reviewed_at",
            "updated_at",
        ]
