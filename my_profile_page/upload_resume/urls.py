from django.urls import path
from .views import SubmitExperienceView,ExperienceListView
app_name = 'upload_resume'

urlpatterns = [

    path('submit/',SubmitExperienceView.as_view(),name='submit'),
    path('resume/',ExperienceListView.as_view(),name='resume'),

]