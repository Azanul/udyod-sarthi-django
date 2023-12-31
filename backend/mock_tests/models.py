from django.db import models
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
    description = models.TextField()
    choices = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=4,
        default=list
    )
    answer = models.IntegerField()

class MockTest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    skills = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
        default=list
    )
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title
