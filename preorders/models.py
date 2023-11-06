""" Data Models for AppVerse.preorders """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class PreOrder(models.Model):
    """App pre-orders"""

    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="Pre-ordered app",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The user that pre-ordered the app",
    )
    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_pre_order_app_user",
                fields=["app", "user"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.app.name} App pre-order by {self.user}"
