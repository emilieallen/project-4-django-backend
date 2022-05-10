from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    message = 'You have to be the author in order to amend this object'

    def has_object_permission(self, request, _view, obj):
        return obj.added_by == request.user

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
       # Authenticated users only can see list view
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user