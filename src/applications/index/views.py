# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_index(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         return render(request, "index/index.html")
from django.views.generic import TemplateView
from applications.index.models import IndexInSubInf


class IndexView(TemplateView):
    template_name = "index/index.html"
    model = IndexInSubInf

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = IndexInSubInf.objects.first()
        ctx = {"ist": info.ist}

        ctx.update(parent_ctx)

        return ctx
    # def get(self, request):
    #     return render(request, "index/index.html")