from django.urls import path

from .views import post_view, PostListView

urlpatterns = [
    path("posts", PostListView.as_view(), name="post_list"),
    path("posts/<int:post_id>", post_view, name="post_detail"),
]