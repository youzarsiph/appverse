""" Serializers for appverse.apps """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.apps.models import App, PlatformApp


# Create your serializers here.
class AppSerializer(HyperlinkedModelSerializer):
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
            "is_paid",
            "price",
            "pre_orderable",
            "contains_purchases",
            "contains_ads",
            "restrictions",
            "created_at",
            "updated_at",
        ]


class DetailedAppSerializer(AppSerializer):
    """App serializer with more details"""

    class Meta(AppSerializer.Meta):
        """Meta data"""

        read_only_fields = AppSerializer.Meta.read_only_fields + [
            "screenshots",
            "reviews",
        ]
        fields = AppSerializer.Meta.fields + [
            "website",
            "privacy_policy",
            "platforms",
            "tags",
            "categories",
            "permissions",
            "screenshots",
            "reviews",
        ]


class Depth1AppSerializer(DetailedAppSerializer):
    """Depth 1 detailed app serializer"""

    class Meta(DetailedAppSerializer.Meta):
        """Meta data"""

        depth = 1


class PlatformAppSerializer(HyperlinkedModelSerializer):
    """Platform App serializer"""

    class Meta:
        """Meta data"""

        model = PlatformApp
        read_only_fields = ["app"]
        fields = [
            "id",
            # "url",
            "app",
            "platform",
            "release_date",
            "version",
            "file",
            "updates",
            "size",
            "released_at",
            "updated_at",
        ]
