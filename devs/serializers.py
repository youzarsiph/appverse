""" Serializers for appverse.devs """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.devs.models import Developer


# Create your serializers here.
class DeveloperSerializer(HyperlinkedModelSerializer):
    """Developer serializer"""

    class Meta:
        """Meta data"""

        model = Developer
        read_only_fields = ["user", "is_approved"]
        fields = [
            "id",
            "url",
            "user",
            "is_approved",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]
