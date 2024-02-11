""" API endpoints for appverse.reviews """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appverse.mixins import OwnerMixin
from appverse.permissions import IsOwner
from appverse.releases.models import Release
from appverse.reviews.models import Review
from appverse.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "release__app__name", "comment"]
    ordering_fields = ["id", "reviewed_at", "updated_at"]
    filterset_fields = ["user", "release__app"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class AppReviewsViewSet(ReviewViewSet):
    """Reviews of an app"""

    def get_queryset(self):
        """Filter queryset by app"""

        release = Release.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(release=release)

    def perform_create(self, serializer):
        """Save report with app and user"""

        release = Release.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, release=release)


class UserReviewsViewSet(ReviewViewSet):
    """Reviews made by a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
