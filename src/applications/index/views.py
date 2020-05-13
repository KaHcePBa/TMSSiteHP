import random

from django.views.generic import TemplateView
from applications.index.models import IndexInSubInf

class IndexView(TemplateView):
    template_name = "index/index.html"
    model = IndexInSubInf

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        randomized_id = random.randrange(2, 7)  # если нужны от 2 до 8

        info = IndexInSubInf.objects.get(id=randomized_id)  # если get не находит объекта - ObjectDoesNotExist
        ctx["ist"] = info.ist

        if ctx["ist"] is None:
            ctx["ist"] = 'Your database is empty or has null strings. Please update!'

        return ctx
