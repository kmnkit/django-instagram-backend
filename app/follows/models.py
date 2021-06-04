from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFollowing(TimeStampedModel):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_followers"
            )
        ]
        ordering = ["-created_at"]
