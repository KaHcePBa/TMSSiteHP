# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_index(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         return render(request, "index/index.html")
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index/index.html"
    # def get(self, request):
    #     return render(request, "index/index.html")
