""" Serializers for appverse.reviews """

from rest_framework.serializers import ModelSerializer
from appverse.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(ModelSerializer):
    """Review serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = ["release", "user"]
        fields = [
            "id",
            "url",
            "release",
            "user",
            "comment",
            "rating",
            "reviewed_at",
            "updated_at",
        ]
