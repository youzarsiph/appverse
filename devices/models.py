""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Manufacturer(models.Model):
    """Device Manufacturer"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Manufacturer name",
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


class Model(models.Model):
    """Device Model"""

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        help_text="Device Manufacturer",
    )
    platform = models.ForeignKey(
        "platforms.Version",
        on_delete=models.CASCADE,
        help_text="Device OS",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Model name",
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
        return f"{self.manufacturer} {self.name}"


class Device(models.Model):
    """User Devices"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="devices",
        help_text="Device Owner",
    )
    model = models.ForeignKey(
        Model,
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
