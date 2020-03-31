from pathlib import Path

from django.contrib import admin
# from django.conf import settings
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()

# PRO_DIR:
# HTML_INDEX: Path = settings.REPO_DIR / "index.html"


def view_index(r):
    HTML_INDEX = here.parent.parent / "index.html"
    with HTML_INDEX.open() as src:
        return HttpResponse(src.read())


def view_resume(r):
    resume = here.parent.parent / "resume.html"
    with resume.open() as src:
        return HttpResponse(src.read())


def view_projects(r):
    projects = here.parent.parent / "projects.html"
    with projects.open() as src:
        return HttpResponse(src.read())


def view_thoughts(r):
    thoughts = here.parent.parent / "thoughts.html"
    with thoughts.open() as src:
        return HttpResponse(src.read())


def view_image(r):
    jpg_me = here.parent.parent / "images/me.jpg"
    with jpg_me.open("rb") as src:
        return HttpResponse(src.read(), content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),  # объект который стоит перед круглой скобкой мы пытаемся вызвать, в д.сл. path
    path('', view_index),
    path('resume/', view_resume),
    path('projects/', view_projects),
    path('thoughts/', view_thoughts),
    path('me/', view_image)
]
