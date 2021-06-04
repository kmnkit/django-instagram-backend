from django.contrib.auth import get_user_model
from rest_framework import serializers as sz
from .models import UserFollowing


class FollowSerializer(sz.ModelSerializer):
    user = sz.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    following = sz.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = UserFollowing
        fields = ("user", "following")

    def create(self, validated_data):
        print(validated_data)