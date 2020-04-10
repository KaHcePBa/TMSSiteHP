from django.urls import path

from apps.thoughts.views import view_thoughts

urlpatterns = [
    path('', view_thoughts),
]
