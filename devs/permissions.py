""" Permissions """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsAppOwner(BasePermission):
    """Check if the current logged in user is the owner of the app"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.developer == obj.developer)
