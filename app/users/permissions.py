from rest_framework.permissions import BasePermission


class IsSelfOrIsStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        print(dir(user))
        if user.is_staff is True or obj == user:
            return True
        return False
