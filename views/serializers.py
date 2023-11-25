""" Serializers for AppVerse.views """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.views.models import View


# Create your serializers here.
class ViewSerializer(HyperlinkedModelSerializer):
    """View serializer"""

    class Meta:
        """Meta data"""

        model = View
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "app", "user", "count", "viewed_at", "reviewed_at"]
