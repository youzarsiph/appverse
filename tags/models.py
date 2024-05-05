""" Data Models for appverse.tags """

from django.db import models


# Create your models here.
class Tag(models.Model):
    """App tags"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Tag name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Tag description",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    @property
    def app_count(self) -> int:
        """Number of apps associated with a tag

        Returns:
            int: number of apps of a tag
        """

        return self.apps.count()

    def __str__(self) -> str:
        return self.name
