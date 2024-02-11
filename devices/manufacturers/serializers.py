""" Serializers for appverse.devices.manufacturers """

from rest_framework.serializers import ModelSerializer
from appverse.devices.manufacturers.models import Manufacturer, Model


# Create your serializers here.
class ManufacturerSerializer(ModelSerializer):
    """Manufacturer serializer"""

    class Meta:
        """Meta data"""

        model = Manufacturer
        fields = [
            "id",
            "url",
            "name",
            "created_at",
            "updated_at",
        ]


class DeviceModelSerializer(ModelSerializer):
    """Device Model serializer"""

    class Meta:
        """Meta data"""

        model = Model
        fields = [
            "id",
            "url",
            "manufacturer",
            "platform",
            "name",
            "created_at",
            "updated_at",
        ]
