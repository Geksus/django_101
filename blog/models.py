from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
