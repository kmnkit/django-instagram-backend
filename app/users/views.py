from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from .serializers import UserSerializer
from .permissions import IsSelfOrIsStaff


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class UserCreateViewSet(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class UserUpdateViewSet(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsSelfOrIsStaff,
    ]


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class UserDeleteView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsSelfOrIsStaff,
    ]
