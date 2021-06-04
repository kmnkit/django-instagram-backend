from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import FollowingSerializer
from .models import UserFollowing


class FollowViewSet(ModelViewSet):
    queryset = UserFollowing.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
