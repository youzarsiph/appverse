""" Serializers for appverse.installs """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.installs.models import Install


# Create your serializers here.
class InstallSerializer(HyperlinkedModelSerializer):
    """Install serializer"""

    class Meta:
        """Meta data"""

        model = Install
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "app", "user", "count", "installed_at", "reinstalled_at"]
