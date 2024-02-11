""" Serializers for appverse.screenshots """

from rest_framework.serializers import ModelSerializer
from appverse.screenshots.models import Screenshot


# Create your serializers here.
class ScreenshotSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Screenshot
        read_only_fields = ["release"]
        fields = [
            "id",
            "url",
            "release",
            "is_trailer",
            "image",
            "video",
            "description",
            "created_at",
            "updated_at",
        ]
