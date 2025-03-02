from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from .models import WorkExperience

class SubmitExperienceView(FormView):
    def get(self, request, *args, **kwargs):
        return render(request, 'upload_resume/submit_experience.html')

    def post(self, request, *args, **kwargs):
        entry_type = request.POST.get('entry_type')
        date = request.POST.get('date')
        job_title = request.POST.get('job_title')
        organization = request.POST.get('organization')
        location = request.POST.get('location')
        description = request.POST.get('description')

        WorkExperience.objects.create(
            typeof=entry_type,
            date=date,
            job_title=job_title,
            organization=organization,
            location=location,
            description=description
        )

        return redirect(reverse_lazy('upload_resume:resume'))


class ExperienceListView(ListView):
    model = WorkExperience
    template_name = 'resume.html'
    context_object_name = 'experiences'
    queryset = WorkExperience.objects.all()
