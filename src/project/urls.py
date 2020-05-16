from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # позволяет входить под админом на свой сайт sakasper.herokuapp.com/admin
    path('', include("applications.index.urls")),
    path('resume/', include("applications.resume.urls")),
    path('projects/', include("applications.projects.urls")),
    path('musicpl/', include("applications.musicpl.urls")),
    path('blog/', include("applications.blog.urls")),
]
