""" Data Models """


from django.db import models


# Create your models here.
class Platform(models.Model):
    """App platform/OS"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Platform name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Platform description",
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
