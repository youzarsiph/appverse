""" Data Models """


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
    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        help_text="Reported app",
    )
    comment = models.CharField(
        max_length=256,
        help_text="What is the problem?",
    )
    updated_at = models.DateTimeField(auto_now=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
