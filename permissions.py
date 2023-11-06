""" Permissions """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Check if the current logged in user is the owner of the object"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user == obj.user)


class IsDeveloper(BasePermission):
    """Check if the current logged in user has a developer profile"""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.developer is not None
            and request.user.developer.is_approved
        )


class IsAppOwner(BasePermission):
    """Check if the current logged in user is the owner of the app"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.developer == obj.developer)


class IsAppObjectOwner(BasePermission):
    """Check if the current logged in user is the owner of the app"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.developer == obj.app.developer)
