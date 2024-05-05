""" Data Models for appverse.apps """

from django.db import models


# Create your models here.
class Category(models.Model):
    """App categories"""

    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Category name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Category description",
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
        """Number of apps in a category

        Returns:
            int: number of apps in a category
        """

        return self.apps.count()

    def __str__(self) -> str:
        return self.name
