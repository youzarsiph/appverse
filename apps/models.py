""" Data Models for appverse.apps """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class App(models.Model):
    """Apps"""

    developer = models.ForeignKey(
        "developers.Developer",
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
    website = models.URLField(
        null=True,
        blank=True,
        help_text="App website",
    )
    platforms = models.ManyToManyField(
        "versions.Version",
        through="releases.Release",
        help_text="App platforms",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        related_name="apps",
        help_text="App tags",
    )
    categories = models.ManyToManyField(
        "categories.Category",
        blank=True,
        related_name="apps",
        help_text="App Categories",
    )
    permissions = models.ManyToManyField(
        "perms.Permission",
        blank=True,
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

    @property
    def platform_count(self) -> int:
        """
        The number of platforms that the app released for

        Returns:
            int: number of app releases
        """

        return self.platforms.count()

    @property
    def category_count(self) -> int:
        """
        The number of categories associated with the app

        Returns:
            int: number of categories of an app
        """

        return self.categories.count()

    @property
    def tag_count(self) -> int:
        """
        The number of tags associated with the app

        Returns:
            int: number of tags of an app
        """

        return self.tags.count()

    @property
    def view_count(self) -> int:
        """
        The number of app views

        Returns:
            int: number of app views
        """

        return sum([view.count for view in self.views.all()])

    @property
    def install_count(self) -> int:
        """
        The number of app installs

        Returns:
            int: number of app installs
        """

        return sum([install.count for install in self.installs.all()])

    def __str__(self) -> str:
        return self.name
