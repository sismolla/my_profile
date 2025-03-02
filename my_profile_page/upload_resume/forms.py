from django import forms
from .models import WorkExperience

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['typeof','date', 'job_title', 'organization', 'location', 'description']
        widgets = {
            
        }
