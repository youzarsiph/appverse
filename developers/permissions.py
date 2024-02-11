""" Permissions """

from rest_framework.permissions import BasePermission
from appverse.developers.models import Developer


# Create your permissions here.
class IsAppOwner(BasePermission):
    """Check if the current logged in user is the owner of the app"""

    def has_object_permission(self, request, view, obj):
        try:
            return bool(
                request.user
                and request.user.developer
                and request.user.developer.is_approved
                and request.user.developer == obj.developer
            )
        except Developer.DoesNotExist:
            return False
