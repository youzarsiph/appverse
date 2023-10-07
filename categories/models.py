""" Data Models """


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
        null=True,
        blank=True,
        help_text="Category description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
