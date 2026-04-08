from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# def post_list(request):
#     posts = Post.objects.all().order_by('text')
#     for post in posts:
#         if len(post.text) > 50:
#             post.text = post.text[:50] + "..."
#     return render(request, 'post_list.html', {'posts': posts})


def post_view(request, post_id):
    single_post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", {"post": single_post})


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
