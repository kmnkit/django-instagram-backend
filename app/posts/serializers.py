from django.contrib.auth import get_user_model
from rest_framework import serializers as sz
from users.serializers import UserSerializer
from .models import Hashtag, Post, Comment
from .utils import save_hashtags


class HashtagSerializer(sz.ModelSerializer):
    """해쉬태그 시리얼라이저"""

    class Meta:
        model = Hashtag
        fields = ("id", "name")
        read_only_fields = ("id",)


class PostSerializer(sz.ModelSerializer):
    """포스트 시리얼라이저"""

    class Meta:
        model = Post
        fields = ("id", "user", "tags", "text")
        read_only_fields = ("id", "user", "tags")

    def create(self, validated_data):
        text = validated_data.get("text")
        tag_list = save_hashtags(text)
        if tag_list:
            tag_obj_list = [Hashtag(name=tag) for tag in tag_list]
            Hashtag.objects.bulk_create(tag_obj_list, ignore_conflicts=True)
        post = Post.objects.create(**validated_data)
        post.save()
        tags = Hashtag.objects.filter(name__in=tag_list)
        post.tags.set(tags)
        return post


class PostDetailSerializer(PostSerializer):
    user = UserSerializer(read_only=True)
    tags = HashtagSerializer(many=True, read_only=True)


class PostImageSerializer(sz.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "image")
        read_only_fields = ("id",)


class CommentSerializer(sz.ModelSerializer):
    post = sz.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "comment")
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        comment = Comment.objects.create(**validated_data, user=user)
        return comment
