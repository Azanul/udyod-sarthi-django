from django.db import models
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    skills_taught = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
        default=[]
    )

    def __str__(self):
        return self.title