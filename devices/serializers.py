""" Serializers for appverse.devices """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.devices.models import Manufacturer, Model, Device


# Create your serializers here.
class ManufacturerSerializer(HyperlinkedModelSerializer):
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


class ModelSerializer(HyperlinkedModelSerializer):
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


class DeviceSerializer(HyperlinkedModelSerializer):
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
