# from pathlib import Path

from django.contrib import admin
# from django.http import HttpResponse
from django.urls import path, include
# from django.conf import settings

# BACKnLOGO: Path = settings.PROJECT_DIR / "backgnd" / "intro-bg.jpg"


# def read_static(fn, ct):  # fn = filename, ct = content type
#     with open(fn, "rb") as src:  # открываем объект (для картинок стоит "rb" - читать в бинарном формате
#         content = src.read()  # читаем открытый объект
#         resp = HttpResponse(content, content_type=ct)  # response
#         return resp  # выполняем


# def view_backgndnlogo(r):
#     return read_static(BACKnLOGO, "image/jpeg", "image/png")




urlpatterns = [
    path('admin/', admin.site.urls),  # позволяет входить под админом на свой сайт sakasper.herokuapp.com/admin
    path('', include("applications.index.urls")),
    path('resume/', include("applications.resume.urls")),
    path('projects/', include("applications.projects.urls")),
    path('thoughts/', include("applications.thoughts.urls")),
    # path('me/', view_image),
    # path('backgnd/', view_backgndnlogo),
    # path('css/', view_css),
]
