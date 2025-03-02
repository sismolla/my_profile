from django.db import models
from django.urls import reverse

class Contact_me(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    phone_number = models.IntegerField()
    message = models.TextField(max_length=400)

    def __str__(self):
        return f'{self.name} - {self.email}'
    
    def get_absolute_url(self):
        return reverse('core:contact')
    

class Comment(models.Model):
    name = models.CharField(max_length=20 ,null=False, blank=False)
    position = models.TextField(max_length=255,null=False, blank=False)
    message = models.TextField(max_length=255,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + self.position 