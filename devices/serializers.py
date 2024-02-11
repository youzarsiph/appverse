""" Serializers for appverse.devices """

from rest_framework.serializers import ModelSerializer
from appverse.devices.models import Device


# Create your serializers here.
class DeviceSerializer(ModelSerializer):
    """Device serializer"""

    class Meta:
        """Meta data"""

        model = Device
        read_only_fields = ["user", "model"]
        fields = [
            "id",
            "url",
            "user",
            "model",
            "created_at",
            "updated_at",
        ]
