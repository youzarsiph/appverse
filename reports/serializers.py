""" Serializers for AppVerse.reports """


from rest_framework.serializers import ModelSerializer
from appverse.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report serializer"""

    class Meta:
        """Meta data"""

        model = Report
        read_only_fields = ["app", "user"]
        fields = ["id", "url", "app", "user", "comment", "reported_at", "updated_at"]
