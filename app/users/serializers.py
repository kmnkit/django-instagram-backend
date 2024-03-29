from follows.serializers import FollowingSerializer, FollowersSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers as sz


class UserSerializer(sz.ModelSerializer):
    """유저 오브젝트 시리얼라이저"""

    following = sz.SerializerMethodField()
    followers = sz.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "name", "following", "followers")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        """유저 작성"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data
