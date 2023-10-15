""" API endpoints for AppVerse.reviews """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.reviews.models import Review
from appverse.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user_username", "app__name", "comment"]
    ordering_fields = ["reviewed_at", "updated_at"]
    filterset_fields = ["user_username", "app__name"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()
