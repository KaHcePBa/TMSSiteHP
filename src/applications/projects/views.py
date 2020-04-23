# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_projects(request: HttpRequest) -> HttpResponse:
#     return render(request, "projects/projects.html")
from django.views.generic import TemplateView


class ProjectsView(TemplateView):
    template_name = "projects/projects.html"
