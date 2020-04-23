from django.urls import path

from applications.thoughts.views import ThoughtsView

urlpatterns = [
    path('', ThoughtsView.as_view()),
]
