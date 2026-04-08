from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "blog_posts"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    context_object_name = "blog_post"


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog_create.html"
    fields = ["title", "body", "author"]


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog_edit.html"
    fields = ["title", "body", "author"]


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog_home')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
