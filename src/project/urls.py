from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

here = Path(__file__).parent.resolve()

HTML_INDEX: Path = here.parent.parent / "index.html"
HTML_RESUME: Path = here.parent.parent / "resume.html"
HTML_PROJECTS: Path = here.parent.parent / "projects.html"
HTML_THOUGHTS: Path = here.parent.parent / "thoughts.html"
JPG_ME: Path = here.parent.parent / "images/me.jpg"


def read_static(fn, ct): # fn = filename, ct = contenttype
    with open(fn, "rb") as src: # открываем объект (для картинок стоит "rb" - читать в бинарном формате
        content = src.read() # читаем открытый объект
        resp = HttpResponse(content, content_type=ct) # response
        return resp # выполняем


def view_index(r):
    return read_static(HTML_INDEX, "text/html")


def view_resume(r):
    return read_static(HTML_RESUME, "text/html")


def view_projects(r):
    return read_static(HTML_PROJECTS, "text/html")


def view_thoughts(r):
    return read_static(HTML_THOUGHTS, "text/html")


def view_image(r):
    return read_static(JPG_ME, "image/jpeg")


# def view_index(r):
#     with HTML_INDEX.open() as src:
#         return HttpResponse(src.read())
#
#
# def view_resume(r):
#     with HTML_RESUME.open() as src:
#         return HttpResponse(src.read())
#
#
# def view_projects(r):
#     with HTML_PROJECTS.open() as src:
#         return HttpResponse(src.read())
#
#
# def view_thoughts(r):
#     with HTML_THOUGHTS.open() as src:
#         return HttpResponse(src.read())
#
#
# def view_image(r):
#     with JPG_ME.open("rb") as src:
#         return HttpResponse(src.read(), content_type="image/jpeg")


urlpatterns = [
    path('admin/', admin.site.urls),  # объект который стоит перед круглой скобкой мы пытаемся вызвать, в д.сл. path
    path('', view_index),
    path('resume/', view_resume),
    path('projects/', view_projects),
    path('thoughts/', view_thoughts),
    path('me/', view_image),
]
