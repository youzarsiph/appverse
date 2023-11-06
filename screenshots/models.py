""" Data Models for AppVerse.screenshots """


from django.db import models


# Create your models here.
class Screenshot(models.Model):
    """App screenshots"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        related_name="screenshots",
        help_text="App",
    )
    image = models.ImageField(
        help_text="App screen",
        upload_to="images/apps/screenshots/",
    )
    description = models.CharField(
        max_length=256,
        help_text="Screenshot description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.app.name} Screenshot {self.pk}"
