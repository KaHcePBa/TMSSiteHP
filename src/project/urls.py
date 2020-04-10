from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.http import HttpRequest
from django.urls import path, include
from django.conf import settings
from django.shortcuts import render


# CSS_FILE: Path = settings.REPO_DIR / "css" / "style.css"
# HTML_INDEX: Path = settings.REPO_DIR / "index.html"
# HTML_RESUME: Path = settings.REPO_DIR / "resume.html"
# HTML_PROJECTS: Path = settings.REPO_DIR / "projects.html"
# HTML_THOUGHTS: Path = settings.REPO_DIR / "thoughts.html"
# JPG_ME: Path = settings.REPO_DIR / "images" / "me.jpg"
# from apps.resume.views import view_resume
# from apps.projects.views import view_projects

BACK_GND: Path = settings.REPO_DIR / "backgnd" / "background.jpg"


def view_thoughts(request: HttpRequest) -> HttpResponse:
    return render(request, "thoughts.html")


def read_static(fn, ct):  # fn = filename, ct = content type
    with open(fn, "rb") as src:  # открываем объект (для картинок стоит "rb" - читать в бинарном формате
        content = src.read()  # читаем открытый объект
        resp = HttpResponse(content, content_type=ct)  # response
        return resp  # выполняем


def view_backgnd(r):
    return read_static(BACK_GND, "image/jpeg")


# def view_css(r):
#     return read_static(CSS_FILE, "text/css")


# def view_index(r):
#     return read_static(HTML_INDEX, "text/html")
#
#
# def view_resume(r):
#     return read_static(HTML_RESUME, "text/html")
#
#
# def view_projects(r):
#     return read_static(HTML_PROJECTS, "text/html")
#
#
# def view_thoughts(r):
#     return read_static(HTML_THOUGHTS, "text/html")


# def view_image(r):
#     return read_static(JPG_ME, "image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),  # позволяет входить под админом на свой сайт sakasper.herokuapp.com/admin
    path('', include("apps.index.urls")),
    path('resume/', include("apps.resume.urls")),
    path('projects/', include("apps.projects.urls")),
    path('thoughts/', view_thoughts),
    # path('me/', view_image),
    path('background/', view_backgnd),
    # path('css/', view_css),
]
