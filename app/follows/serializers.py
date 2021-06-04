from rest_framework import serializers as sz
from .models import UserFollowing


class FollowingSerializer(sz.ModelSerializer):
    """유저가 Follow 하는 리스트의 시리얼라이저"""

    class Meta:
        model = UserFollowing
        fields = ("id", "following", "created_at")

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        target_user = validated_data.get("following")
        if target_user == user:
            raise sz.ValidationError("셀프 팔로잉은 불가능합니다.")
        following = UserFollowing.objects.create(**validated_data, user=user)
        return following


class FollowersSerializer(sz.ModelSerializer):
    """유저를 Follow 하는 리스트의 시리얼라이저"""

    class Meta:
        model = UserFollowing
        fields = ("id", "user", "created_at")
