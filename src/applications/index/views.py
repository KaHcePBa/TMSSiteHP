# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_index(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         return render(request, "index/index.html")
import random

from django.views.generic import TemplateView
from applications.index.models import IndexInSubInf
# from django.core.exceptions import ObjectDoesNotExist


class IndexView(TemplateView):
    template_name = "index/index.html"
    model = IndexInSubInf

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # try:
        #     randomized_id = IndexInSubInf.objects.get(id=5)
        #     randomized_id = IndexInSubInf.objects.get(id=4)
        # except ObjectDoesNotExist:
        #     pass

        randomized_id = random.randrange(1, 4) # если нужны от 1 до 3

        info = IndexInSubInf.objects.get(id=randomized_id)
        ctx["ist"] = info.ist

        if ctx["ist"] is None:
            ctx["ist"] = 'Your database is empty. Please update!'

        return ctx
    # def get(self, request):
    #     return render(request, "index/index.html")
