import random

from django.views.generic import TemplateView
from applications.index.models import IndexInSubInf
from applications.index.models import YanGooAnalytics


class IndexView(TemplateView):
    template_name = "index/index.html"
    model = IndexInSubInf

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        randomized_id = random.randrange(2, 7)  # если нужны от 2 до 8

        try:
            info = IndexInSubInf.objects.get(id=randomized_id)  # если get не находит объекта - ObjectDoesNotExist
        except IndexInSubInf.DoesNotExist:
            info = None # AttributeError: 'NoneType' object has no attribute 'ist'

        if info is None:
            return ctx

        ctx["ist"] = info.ist
        return ctx

# class MetriksView(TemplateView):
#     template_name = "index/index.html"
#     model = YanGooAnalytics
#     context_object_name = "type_metrika"
#
#     def getm_context_data(self, **kwargs):
#         mtx = super().getm_context_data(self, **kwargs)
#
#         info_mtx = YanGooAnalytics.objects.all()
#
#         mtx["code_metrika"] = info_mtx.code_metrika
#         return mtx

