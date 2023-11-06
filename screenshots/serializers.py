""" Serializers for AppVerse.screenshots """


from rest_framework.serializers import ModelSerializer
from appverse.screenshots.models import Screenshot


# Create your serializers here.
class ScreenshotSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Screenshot
        read_only_fields = ["app"]
        fields = [
            "id",
            "url",
            "app",
            "image",
            "description",
            "created_at",
            "updated_at",
        ]
