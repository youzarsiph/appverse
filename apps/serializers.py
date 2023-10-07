""" Serializers for AppVerse.apps """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.apps.models import Permission, App, Screenshot


# Create your serializers here.
class PermissionSerializer(HyperlinkedModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Permission
        fields = ["id", "url", "name", "description", "created_at", "updated_att"]


class AppSerializer(HyperlinkedModelSerializer):
    """App serializer"""

    class Meta:
        """Meta data"""

        model = App
        fields = [
            "id",
            "url",
            "developer",
            "icon",
            "cover",
            "name",
            "headline",
            "description",
            "size",
            "paid",
            "purchases",
            "ads",
            "restrictions",
            "version",
            "updates",
            "released_at",
            "updated_at",
            "website",
            "platforms",
            "tags",
            "categories",
            "permissions",
            "privacy_policy",
            "privacy_policy",
        ]


class ScreenshotSerializer(HyperlinkedModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Screenshot
        fields = ["id", "url", "image", "description", "created_at", "updated_at"]
