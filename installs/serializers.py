""" Serializers for AppVerse.installs """


from rest_framework.serializers import ModelSerializer
from appverse.installs.models import Install


# Create your serializers here.
class InstallSerializer(ModelSerializer):
    """Install serializer"""

    class Meta:
        """Meta data"""

        model = Install
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "app", "user", "installed_at", "reinstalled_at"]
