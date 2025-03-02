from django.db import models
from django.urls import reverse

# Create your models here.
class Certificate(models.Model):
    issued_date = models.DateTimeField()
    issued_for = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    image = models.FileField(upload_to='Certificate/')

    def __str__(self):
        return self.issued_for
    
    def get_absolute_url(self):
        return reverse('Certificates:certificate')