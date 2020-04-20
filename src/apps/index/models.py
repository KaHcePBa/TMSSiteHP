from django.db import models as m


class IndexInSubInf(m.Model):
    ist = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Intro Subtitle Info'

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.pk}, ist={self.ist!r})"