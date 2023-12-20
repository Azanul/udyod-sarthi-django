from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disability_category = models.CharField(max_length=26)
    no_posts = models.DecimalField(null=True, blank=True)

    def __str__(self):
        return self.title