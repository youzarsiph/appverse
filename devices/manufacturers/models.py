""" Data Models for appverse.devices.manufacturers """

from django.db import models


# Create your models here.
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
        "platforms.Platform",
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
