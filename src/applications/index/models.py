from django.db import models as m


class IndexInSubInf(m.Model):
    ist = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Intro Subtitle Info'

    def __str__(self):
        return f"({self.pk}, {self.ist!r})"


class YanGooAnalytics(m.Model):
    type_metrika = m.TextField(null=False, blank=True, primary_key=True)
    code_metrika = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Code YanGoo Analytics'

    def __str__(self):
        return f"({self.pk}, {self.code_metrika!r})"
