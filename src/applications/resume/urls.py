from django.urls import path

from applications.resume.apps import ResumeConfig
from applications.resume.views import IndexView

app_name = ResumeConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
