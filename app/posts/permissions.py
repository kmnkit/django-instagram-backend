from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, _, obj):
        user = request.user
        if obj.user == user:
            return True
        return False
