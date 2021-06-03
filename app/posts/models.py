import os
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from core.models import TimeStampedModel

User = get_user_model()


def post_image_file_path(instance, filename):
    """Post의 사진 파일이 올라갈 Path를 생성함"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("uploads/post", filename)


class Hashtag(TimeStampedModel):
    """Hashtag 모델. 공공이라 유저를 따로 두지 않음"""

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    """Post 모델"""

    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField("Hashtag")
    image = models.ImageField(null=True, upload_to=post_image_file_path)
    text = models.TextField(max_length=500)

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.text


class Comment(TimeStampedModel):
    """댓글 모델"""

    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.SET_NULL, null=True
    )
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(max_length=140)

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.user.name}이 {self.created_at}에 작성한 코멘트"
