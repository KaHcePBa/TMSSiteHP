from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_projects(request: HttpRequest) -> HttpResponse:
    return render(request, "projects/projects.html")