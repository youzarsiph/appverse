""" Serializers for AppVerse.reports """


from rest_framework.serializers import HyperlinkedModelSerializer
from appverse.reports.models import Report


# Create your serializers here.
class ReportSerializer(HyperlinkedModelSerializer):
    """Report serializer"""

    class Meta:
        """Meta data"""

        model = Report
        fields = ["id", "url", "user", "app", "comment", "reported_at", "updated_at"]
