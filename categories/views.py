""" API endpoints for AppVerse.categories """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.categories.models import Category
from appverse.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    """CategoryViewSet: Create, view, update and delete Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["name"]
