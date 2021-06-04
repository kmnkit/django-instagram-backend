from rest_framework import viewsets, mixins, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    HashtagSerializer,
    PostSerializer,
    PostDetailSerializer,
    PostImageSerializer,
    CommentSerializer,
)
from .models import Hashtag, Post, Comment
from .permissions import IsOwner


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
        elif self.action == "post_comment" or self.action == "get_comments":
            return CommentSerializer
        return self.serializer_class

    def get_permissions(self):
        if (
            self.action == "list"
            or self.action == "retrieve"
            or self.action == "get_comments"
        ):
            permission_classes = [
                permissions.AllowAny,
            ]
        elif self.action == "create" or self.action == "post_comment":
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
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["POST"], detail=True, url_path="post-comment")
    def post_comment(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=True, url_path="comments")
    def get_comments(self, _, pk=None):
        comments = Comment.objects.filter(post__pk=pk)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
