""" Serializers for AppVerse.reports """


from rest_framework.serializers import ModelSerializer
from appverse.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report serializer"""

    class Meta:
        """Meta data"""

        model = Report
        fields = ["id", "url", "comment", "reported_at", "updated_at"]
