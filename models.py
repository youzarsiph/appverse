""" Data Models for appverse """

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """AppVerse Users"""

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/users/",
        help_text="User profile image",
    )
