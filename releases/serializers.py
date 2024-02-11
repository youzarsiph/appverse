""" Serializers for appverse.releases """

from rest_framework.serializers import ModelSerializer
from appverse.releases.models import Release


# Create your serializers here.
class ReleaseSerializer(ModelSerializer):
    """Release serializer"""

    class Meta:
        """Meta data"""

        model = Release
        read_only_fields = ["app"]
        fields = [
            "id",
            "url",
            "app",
            "platform",
            "is_paid",
            "price",
            "is_orderable",
            "contains_purchases",
            "contains_ads",
            "release_date",
            "version",
            "file",
            "updates",
            "size",
            "released_at",
            "updated_at",
        ]
