""" Serializers for appverse.apps """

from rest_framework.serializers import ModelSerializer
from appverse.apps.models import App


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
            "restrictions",
            "view_count",
            "install_count",
            "created_at",
            "updated_at",
        ]


class RetrievedAppSerializer(AppSerializer):
    """App serializer with more details"""

    class Meta(AppSerializer.Meta):
        """Meta data"""

        fields = AppSerializer.Meta.fields + [
            "website",
            "tags",
            "platforms",
            "categories",
            "permissions",
        ]


class Depth1AppSerializer(RetrievedAppSerializer):
    """Depth 1 detailed app serializer"""

    class Meta(RetrievedAppSerializer.Meta):
        """Meta data"""

        depth = 1
