""" Data Models for AppVerse.screenshots """


from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Screenshot(models.Model):
    """App screenshots"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        related_name="screenshots",
        help_text="App",
    )
    is_trailer = models.BooleanField(
        default=False,
        help_text="Designates if this item is a trailer",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="App screenshot",
        upload_to="images/apps/screenshots/",
    )
    video = models.FileField(
        null=True,
        blank=True,
        help_text="Trailer video",
        upload_to="images/apps/screenshots/trailers/",
        validators=[FileExtensionValidator(["mp4"], "The file format is incorrect!")],
    )
    description = models.CharField(
        max_length=256,
        help_text="Screenshot description",
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
        return f"{self.app.name} Screenshot {self.pk}"
