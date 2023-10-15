""" Serializers for AppVerse.perms """


from rest_framework.serializers import ModelSerializer
from appverse.perms.models import Permission


# Create your serializers here.
class PermissionSerializer(ModelSerializer):
    """Screenshot serializer"""

    class Meta:
        """Meta data"""

        model = Permission
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
