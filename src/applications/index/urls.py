from django.urls import path

from applications.index.views import IndexView
from applications.index.apps import IndexConfig

app_name = IndexConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
