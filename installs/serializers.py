""" Serializers for appverse.installs """

from rest_framework.serializers import ModelSerializer
from appverse.installs.models import Install


# Create your serializers here.
class InstallSerializer(ModelSerializer):
    """App Install serializer"""

    class Meta:
        """Meta data"""

        model = Install
        read_only_fields = ["app", "user", "device"]
        fields = [
            "id",
            "url",
            "app",
            "user",
            "device",
            "is_installed",
            "count",
            "installed_at",
            "reinstalled_at",
        ]
