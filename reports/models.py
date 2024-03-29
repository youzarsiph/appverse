""" Data Models for appverse.reports """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Report(models.Model):
    """Abuse reports"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Reporter",
    )
    release = models.ForeignKey(
        "releases.Release",
        on_delete=models.CASCADE,
        help_text="Reported app",
    )
    comment = models.CharField(
        max_length=256,
        help_text="What is the problem?",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    reported_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date reported",
    )

    def __str__(self) -> str:
        return f"{self.release.app.name}:{self.release.platform.name} App report by {self.user}"
