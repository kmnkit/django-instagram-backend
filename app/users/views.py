from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from .serializers import UserSerializer
from .permissions import IsSelfOrIsStaff


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if (
            self.action == "update"
            or self.action == "partial_update"
            or self.action == "destroy"
        ):
            permission_classes = [
                IsSelfOrIsStaff,
            ]
        elif self.action == "follow":
            permission_classes = [
                permissions.IsAuthenticated,
            ]
        else:
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]
