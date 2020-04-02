from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()


def view_index(r):
    HTML_INDEX = here.parent.parent / "index.html"
    with HTML_INDEX.open() as src:
        return HttpResponse(src.read())


def view_resume(r):
    HTML_RESUME = here.parent.parent / "resume.html"
    with HTML_RESUME.open() as src:
        return HttpResponse(src.read())


def view_projects(r):
    HTML_PROJECTS = here.parent.parent / "projects.html"
    with HTML_PROJECTS.open() as src:
        return HttpResponse(src.read())


def view_thoughts(r):
    HTML_THOUGHTS = here.parent.parent / "thoughts.html"
    with HTML_THOUGHTS.open() as src:
        return HttpResponse(src.read())


def view_image(r):
    JPG_ME = here.parent.parent / "images/me.jpg"
    with JPG_ME.open("rb") as src:
        return HttpResponse(src.read(), content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),  # объект который стоит перед круглой скобкой мы пытаемся вызвать, в д.сл. path
    path('', view_index),
    path('resume/', view_resume),
    path('projects/', view_projects),
    path('thoughts/', view_thoughts),
    path('me/', view_image),
]
