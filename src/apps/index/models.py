from django.db import models as m


class IndexIntroSubtitleInfo(m.Model):
    introsubtitle = m.TextField(null=True, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Intro Subtitle Info'

    def __str__(self):
        return f"IndexIntroSubtitleInfo(introsubtitle={self.introsubtitle})"