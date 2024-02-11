""" Serializers for appverse.views """

from rest_framework.serializers import ModelSerializer
from appverse.views.models import View


# Create your serializers here.
class ViewSerializer(ModelSerializer):
    """View serializer"""

    class Meta:
        """Meta data"""

        model = View
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "app", "user", "count", "viewed_at", "reviewed_at"]
