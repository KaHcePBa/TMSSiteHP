from django.urls import path

from applications.resume.views import ResumeView

urlpatterns = [
    path('', ResumeView.as_view()),
]
