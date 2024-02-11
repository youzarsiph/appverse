""" Data Models for appverse.releases """

from django.db import models


# Create your models here.
class Release(models.Model):
    """App release for a platform"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="The app",
    )
    platform = models.ForeignKey(
        "versions.Version",
        on_delete=models.CASCADE,
        help_text="The platform",
    )
    is_paid = models.BooleanField(
        default=False,
        help_text="Designates if the app is paid",
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="App price if it's paid",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the app is approved by AppVerse",
    )
    is_orderable = models.BooleanField(
        default=False,
        help_text="Designates if the app is pre-orderable",
    )
    contains_purchases = models.BooleanField(
        default=False,
        help_text="Designates if the app contains in-app purchases",
    )
    contains_ads = models.BooleanField(
        default=False,
        help_text="Designates if the app contains ads",
    )
    release_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="App release date if the app is not released yet",
    )
    version = models.CharField(
        max_length=8,
        default="0.00",
        help_text="App Version",
    )
    file = models.FileField(
        upload_to="apps/",
        help_text="App's executable",
    )
    updates = models.TextField(
        help_text="What is new?",
    )
    size = models.FloatField(
        default=0.0,
        help_text="Download size in MBs",
    )
    released_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Release date",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_app_platform",
                fields=["app", "platform"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.app.name} App for {self.platform.name}"
