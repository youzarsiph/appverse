""" Serializers for appverse.screenshots """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.screenshots.models import Screenshot


# Create your serializers here.
class ScreenshotSerializer(HyperlinkedModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Screenshot
        read_only_fields = ["app"]
        fields = [
            "id",
            "url",
            "app",
            "is_trailer",
            "image",
            "video",
            "description",
            "created_at",
            "updated_at",
        ]
