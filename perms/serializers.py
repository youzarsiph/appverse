""" Serializers for appverse.perms """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.perms.models import Permission


# Create your serializers here.
class PermissionSerializer(HyperlinkedModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Permission
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
