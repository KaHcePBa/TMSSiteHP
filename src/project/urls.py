from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # позволяет входить под админом на свой сайт sakasper.herokuapp.com/admin
    path('', include("applications.index.urls")),
    path('resume/', include("applications.resume.urls")),
    path('projects/', include("applications.projects.urls")),
    path('thoughts/', include("applications.thoughts.urls")),
    path('blog/', include("applications.blog.urls")),
]
