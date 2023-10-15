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
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Permission description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
