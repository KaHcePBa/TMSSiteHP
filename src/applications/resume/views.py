# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View

# def view_resume(request: HttpRequest) -> HttpResponse:
#     return render(request, "resume/resume.html")
from django.views.generic import TemplateView


class ResumeView(TemplateView):
    template_name = "resume/resume.html"
