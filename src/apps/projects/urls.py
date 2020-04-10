from django.urls import path

from apps.projects.views import view_projects

urlpatterns = [
    path('', view_projects),
]
