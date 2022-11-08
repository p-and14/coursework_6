from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')


class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            view.action == "list"
        )


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.method in SAFE_METHODS or
            obj.author == request.user
        )
