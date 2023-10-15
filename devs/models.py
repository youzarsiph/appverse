""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Developer(models.Model):
    """Developer profiles"""

    # The user
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="The owner of developer account",
    )
    image = models.ImageField(
        upload_to="images/developers/",
        help_text="Developer profile photo",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Developer name",
    )
    headline = models.CharField(
        max_length=256,
        help_text="Developer headline",
    )
    description = models.TextField(
        help_text="Description",
    )
    approved = models.BooleanField(
        default=False,
        help_text="Designates if the developer account is approved by AppVerse",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
