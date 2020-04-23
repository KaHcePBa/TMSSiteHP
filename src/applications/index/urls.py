from django.urls import path

from applications.index.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
