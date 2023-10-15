""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Review(models.Model):
    """App reviews"""

    # The reviewer
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Reviewer",
    )
    # The reviewed app
    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="Reviewed app",
    )
    comment = models.CharField(
        max_length=256,
        help_text="App review",
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        help_text="App rating",
        choices=[
            (1, "Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
    )
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
