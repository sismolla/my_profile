from django.db import models

class WorkExperience(models.Model):
    typeof = models.CharField(max_length=30)
    date = models.CharField(max_length=4, help_text="Year of experience")
    job_title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.organization}"
