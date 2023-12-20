from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django import models

class EndUser(User):
    saved_query = ArrayField(
        models.CharField(
            models.CharField(max_length=255, blank=True),
            size=8,
            default=list
        )
    )
