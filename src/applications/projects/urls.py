from django.urls import path

from applications.projects.views import ProjectsView

urlpatterns = [
    path('', ProjectsView.as_view()),
]
