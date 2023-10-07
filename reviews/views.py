""" API endpoints for AppVerse.reviews """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from appverse.reviews.models import Review
from appverse.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(ModelViewSet):
    """ReviewViewSet: Create, view, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    search_fields = ["user_username", "app__name", "comment"]
    ordering_fields = ["reviewed_at", "updated_at"]
    filterset_fields = ["user_username", "app__name"]
