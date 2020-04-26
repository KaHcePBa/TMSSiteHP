from django.urls import path

from applications.thoughts.apps import ThoughtsConfig
from applications.thoughts.views import IndexView

app_name = ThoughtsConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
