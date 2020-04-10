# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_thoughts(request: HttpRequest) -> HttpResponse:
#     return render(request, "thoughts/thoughts.html")
from django.views.generic import TemplateView


class ThoughtsView(TemplateView):
    template_name = "thoughts/thoughts.html"
