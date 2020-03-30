from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()


def view_index():
    index = here.parent.parent / "index.html"
    with index.open() as src:
        return HttpResponse(src.read())


def view_resume():
    resume = here.parent.parent / "resume.html"
    with resume.open() as src:
        return HttpResponse(src.read())


def view_projects():
    projects = here.parent.parent / "projects.html"
    with projects.open() as src:
        return HttpResponse(src.read())


def view_thoughts():
    thoughts = here.parent.parent / "thoughts.html"
    with thoughts.open() as src:
        return HttpResponse(src.read())


def view_image():
    jpg_me = here.parent.parent / "images/me.jpg"
    with jpg_me.open("rb") as src:
        return HttpResponse(src.read(), content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index),
    path('resume/', view_resume),
    path('projects/', view_projects),
    path('thoughts/', view_thoughts),
    path('me/', view_image)
]
