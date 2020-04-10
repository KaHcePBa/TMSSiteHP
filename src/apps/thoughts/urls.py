from django.urls import path

from apps.thoughts.views import ThoughtsView

urlpatterns = [
    path('', ThoughtsView.as_view()),
]
