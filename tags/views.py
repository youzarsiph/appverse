""" API endpoints for AppVerse.tags """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.tags.models import Tag
from appverse.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    """TagViewSet: Create, view, update and delete Tags"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["name"]
