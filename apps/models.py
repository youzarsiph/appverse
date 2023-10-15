""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


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
        upload_to="images/icons/",
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
    description = models.TextField(
        null=True,
        blank=True,
        help_text="App description",
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="App price (if it's paid)",
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
    privacy_policy = models.TextField(
        help_text="Privacy policy",
    )
    website = models.URLField(
        null=True,
        blank=True,
        help_text="App website",
    )
    # Platform that the app is built for
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
    released_at = models.DateTimeField(
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
        upload_to="images/screenshots/",
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
    )
    installed_at = models.DateTimeField(auto_now_add=True)
    reinstalled_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_install_app_user",
                fields=["app", "user"],
            )
        ]


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
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_view_app_user",
                fields=["app", "user"],
            )
        ]
