from django.contrib import admin

# Register your models here.
from .models import Contact_me,Comment

admin.site.register(Contact_me)
admin.site.register(Comment)