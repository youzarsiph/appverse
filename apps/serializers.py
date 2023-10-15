""" Serializers for AppVerse.apps """


from rest_framework.serializers import ModelSerializer
from appverse.apps.models import App, PlatformApp, Screenshot


# Create your serializers here.
class AppSerializer(ModelSerializer):
    """App serializer"""

    class Meta:
        """Meta data"""

        depth = 1
        model = App
        read_only_fields = ["developer"]
        # extra_kwargs = {}
        fields = [
            "id",
            "url",
            "developer",
            "icon",
            "cover",
            "name",
            "headline",
            "description",
            "paid",
            "purchases",
            "ads",
            "restrictions",
            "released_at",
            "updated_at",
            "website",
            "platforms",
            "tags",
            "categories",
            "permissions",
            "privacy_policy",
            "screenshot_set",
        ]


class PlatformAppSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        depth = 1
        model = PlatformApp
        fields = [
            "id",
            "platform",
            "version",
            "file",
            "updates",
            "size",
            "released_at",
            "updated_at",
        ]


class ScreenshotSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Screenshot
        fields = ["id", "url", "image", "description", "created_at", "updated_at"]
