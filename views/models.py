""" Data Models for appverse.views """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class View(models.Model):
    """App views"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="Viewed app",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The viewer",
    )
    count = models.PositiveIntegerField(
        default=0,
        help_text="View count",
    )
    viewed_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date viewed",
    )
    reviewed_at = models.DateTimeField(
        auto_now=True,
        help_text="Last viewed",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_view_app_user",
                fields=["app", "user"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.app.name} App view by {self.user}"
