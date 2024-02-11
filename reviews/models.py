""" Data Models """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Review(models.Model):
    """App reviews"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Reviewer",
    )
    release = models.ForeignKey(
        "releases.Release",
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text="Reviewed app",
    )
    comment = models.CharField(
        max_length=256,
        help_text="App review",
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        help_text="App rating",
        choices=[
            (1, "Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    reviewed_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date reviewed",
    )

    def __str__(self) -> str:
        return f"{self.release.app.name}:{self.release.platform.name} App review by {self.user}"
