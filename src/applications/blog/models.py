from django.db import models
from django.urls import reverse_lazy


class BlogPost(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})
        # return f"/blog/post/{self:pk}/"