import re
from rest_framework import viewsets, mixins, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import (
    HashtagSerializer,
    PostSerializer,
    PostDetailSerializer,
    PostImageSerializer,
)
from .models import Hashtag, Post
from .permissions import IsOwner
from .utils import save_hashtags


class HashtagViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        elif self.action == "upload_image":
            return PostImageSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [
                permissions.AllowAny,
            ]
        elif self.action == "create":
            permission_classes = [
                permissions.IsAuthenticated,
            ]
        else:
            permission_classes = [
                IsOwner,
            ]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request, pk=None):
        """Upload an image to a recipe"""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
