""" Data Models """

from django.db import models


# Create your models here.
class Permission(models.Model):
    """Permissions required by the app"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Permission name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Permission description",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    def __str__(self) -> str:
        return self.name
