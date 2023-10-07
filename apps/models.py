""" Data Models """


from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Permission(models.Model):
    """Permissions required by the app"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Permission name",
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Permission description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class App(models.Model):
    """Apps"""

    # The developer of the app
    developer = models.ForeignKey(
        "devs.Developer",
        on_delete=models.CASCADE,
        help_text="App developer",
    )
    icon = models.ImageField(
        help_text="App icon",
        upload_to="images/covers/",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        help_text="App cover",
        upload_to="images/covers/",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="App name",
    )
    headline = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="App headline",
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="App description",
    )
    file = models.FileField(
        upload_to="apps/",
        help_text="App package",
    )
    size = models.FloatField(
        default=0.0,
        help_text="Download size in MBs",
    )
    paid = models.BooleanField(
        default=False,
        help_text="Designates if the app is paid",
    )
    purchases = models.BooleanField(
        default=False,
        help_text="Designates if the app contains in-app purchases",
    )
    ads = models.BooleanField(
        default=False,
        help_text="Designates if the app contains ads",
    )
    approved = models.BooleanField(
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
    version = models.FloatField(
        default=0.1,
        help_text="App Version",
    )
    updates = models.TextField(
        null=True,
        blank=True,
        help_text="What is new?",
    )
    privacy_policy = models.TextField(
        null=True,
        blank=True,
        help_text="Privacy policy",
    )
    released_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Release date",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Last update",
    )
    website = models.URLField(
        null=True,
        blank=True,
        help_text="App website",
    )
    # Platform that the app is built for
    platforms = models.ManyToManyField(
        "platforms.Platform",
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
        "Permission",
        help_text="App Permissions",
    )
    installs = models.ManyToManyField(
        User,
        through="Install",
        related_name="installs",
        help_text="App Installs",
    )
    views = models.ManyToManyField(
        User,
        through="View",
        related_name="views",
        help_text="App Views",
    )

    def __str__(self):
        return self.name


class Screenshot(models.Model):
    """App screenshots"""

    # The app
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        help_text="App",
    )
    image = models.ImageField(
        help_text="App screen",
        upload_to="images/screens/",
    )
    description = models.CharField(
        max_length=256,
        help_text="Screenshot description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.app.name} Screenshot {self.pk}"


class Install(models.Model):
    """App installs"""

    # Installed app
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        help_text="Installed app",
    )
    # Installed by
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Installed by",
    )
    count = models.PositiveIntegerField(
        default=1,
        help_text="Install count",
        validators=[
            validators.MinValueValidator(
                0, "Ensure that this field is greater than or equal to 0."
            )
        ],
    )
    installed_at = models.DateTimeField(auto_now_add=True)


class View(models.Model):
    """App views"""

    # Viewed app
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        help_text="Viewed app",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The viewer",
    )
    count = models.PositiveIntegerField(
        default=1,
        help_text="View count",
        validators=[
            validators.MinValueValidator(
                0, "Ensure that this field is greater than or equal to 0."
            )
        ],
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
