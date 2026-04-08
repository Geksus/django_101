from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_home"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
    path('blog/create/', BlogCreateView.as_view(), name="blog_create"),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name="blog_delete"),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name="blog_update"),
]