""" Data Models for appverse.installs """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Install(models.Model):
    """App installs"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="Installed app",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Installed by",
    )
    device = models.ForeignKey(
        "devices.Device",
        on_delete=models.CASCADE,
        help_text="Installed on",
    )
    is_installed = models.BooleanField(
        default=False,
        help_text="Designates if the is installed on the device",
    )
    count = models.PositiveIntegerField(
        default=0,
        help_text="Install count",
    )
    installed_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date installed",
    )
    reinstalled_at = models.DateTimeField(
        auto_now=True,
        help_text="Date reinstalled",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_install_app_user",
                fields=["app", "user", "device"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.app.name} App install by {self.user}"
