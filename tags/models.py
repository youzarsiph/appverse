""" Data Models """


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
        null=True,
        blank=True,
        help_text="Tag description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
