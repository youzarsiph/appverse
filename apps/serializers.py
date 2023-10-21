""" Serializers for AppVerse.apps """


from rest_framework.serializers import ModelSerializer
from appverse.apps.models import App, PlatformApp, Screenshot


# Create your serializers here.
class AppSerializer(ModelSerializer):
    """App serializer"""

    class Meta:
        """Meta data"""

        model = App
        read_only_fields = ["developer"]
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
        ]


class DetailedAppSerializer(AppSerializer):
    """App serializer with more details"""

    class Meta(AppSerializer.Meta):
        """Meta data"""

        # depth = 1
        model = App
        read_only_fields = ["developer"]
        fields = AppSerializer.Meta.fields + [
            "website",
            "privacy_policy",
            "platforms",
            "tags",
            "categories",
            "permissions",
            "screenshots",
        ]


class PlatformAppSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

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
        fields = ["id", "platform", "image", "description", "created_at", "updated_at"]
