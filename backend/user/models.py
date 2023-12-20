from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

class EndUser(AbstractUser):
    saved_query = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
        default=list
    )
