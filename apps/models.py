""" Data Models for AppVerse.apps """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class App(models.Model):
    """Apps"""

    developer = models.ForeignKey(
        "devs.Developer",
        on_delete=models.CASCADE,
        help_text="App developer",
    )
    icon = models.ImageField(
        help_text="App icon",
        upload_to="images/apps/icons/",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        help_text="App cover",
        upload_to="images/apps/covers/",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="App name",
    )
    headline = models.CharField(
        max_length=128,
        help_text="App headline",
    )
    description = models.CharField(
        max_length=256,
        help_text="App description",
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="App price if it's paid",
    )
    is_paid = models.BooleanField(
        default=False,
        help_text="Designates if the app is paid",
    )
    pre_orderable = models.BooleanField(
        default=False,
        help_text="Designates if the app is pre-orderable",
    )
    release_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="App release date if the app is not released yet",
    )
    contains_purchases = models.BooleanField(
        default=False,
        help_text="Designates if the app contains in-app purchases",
    )
    contains_ads = models.BooleanField(
        default=False,
        help_text="Designates if the app contains ads",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the app is approved by AppVerse",
    )
    restrictions = models.PositiveSmallIntegerField(
        default=3,
        help_text="Determines which ages this app is suitable for",
        choices=[
            (3, "Rated 3+"),
            (7, "Rated 7+"),
            (12, "Rated 12+"),
            (16, "Rated 16+"),
            (18, "Rated 18+"),
        ],
    )
    privacy_policy = models.TextField(
        help_text="Privacy policy",
    )
    website = models.URLField(
        null=True,
        blank=True,
        help_text="App website",
    )
    platforms = models.ManyToManyField(
        "platforms.Platform",
        through="PlatformApp",
        help_text="App platforms",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text="App tags",
    )
    categories = models.ManyToManyField(
        "categories.Category",
        help_text="App Categories",
    )
    permissions = models.ManyToManyField(
        "perms.Permission",
        help_text="App Permissions",
    )
    installs = models.ManyToManyField(
        User,
        through="installs.Install",
        related_name="installs",
        help_text="App Installs",
    )
    views = models.ManyToManyField(
        User,
        through="views.View",
        related_name="views",
        help_text="App Views",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Release date",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Last update",
    )

    def __str__(self):
        return self.name


class PlatformApp(models.Model):
    """App's executable for a platform"""

    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        help_text="The app",
    )
    platform = models.ForeignKey(
        "platforms.Platform",
        on_delete=models.CASCADE,
        help_text="The platform",
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
