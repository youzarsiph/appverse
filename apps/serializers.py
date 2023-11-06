""" Serializers for AppVerse.apps """


from rest_framework.serializers import ModelSerializer
from appverse.apps.models import App, PlatformApp


# Create your serializers here.
class AppSerializer(ModelSerializer):
    """App serializer"""

    class Meta:
        """Meta data"""

        model = App
        read_only_fields = ["developer", "is_approved"]
        fields = [
            "id",
            "url",
            "developer",
            "is_approved",
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

        read_only_fields = AppSerializer.Meta.read_only_fields + ["screenshots"]
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
        read_only_fields = ["app"]
        fields = [
            "id",
            # "url",
            "app",
            "platform",
            "version",
            "file",
            "updates",
            "size",
            "released_at",
            "updated_at",
        ]
