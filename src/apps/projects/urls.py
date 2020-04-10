from django.urls import path

from apps.projects.views import ProjectsView

urlpatterns = [
    path('', ProjectsView.as_view()),
]
