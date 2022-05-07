from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    message = 'You have to be the author in order to amend this object'

    def has_object_permission(self, request, _view, obj):
        return obj.added_by == request.user