""" Permissions """


from rest_framework.permissions import BasePermission, SAFE_METHODS
from appverse.devs.models import Developer


# Create your permissions here.
class IsOwner(BasePermission):
    """Check if the current logged in user is the owner of the object"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user == obj.user)


class IsDeveloper(BasePermission):
    """Check if the current logged in user has a developer profile"""

    def has_permission(self, request, view):
        try:
            return bool(
                request.user
                and request.user.developer
                and request.user.developer.is_approved
            )
        except Developer.DoesNotExist:
            return False


class IsAppOwner(BasePermission):
    """Check if the current logged in user is the owner of the app"""

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user
            and request.user.developer
            and request.user.developer.is_approved
            and request.user.developer == obj.developer
        )


class IsAppObjectOwner(BasePermission):
    """Check if the current logged in user is the owner of the app of the object"""

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user
            and request.user.developer
            and request.user.developer.is_approved
            and request.user.developer == obj.app.developer
        )


class IsReadOnly(BasePermission):
    """Allow only if the request is read only"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
