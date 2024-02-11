""" Data Models """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Device(models.Model):
    """User Devices"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="devices",
        help_text="Device Owner",
    )
    model = models.ForeignKey(
        "manufacturers.Model",
        on_delete=models.CASCADE,
        help_text="Device Model",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date registered",
    )

    def __str__(self) -> str:
        return f"{self.user}'s {self.model}"
