from django.urls import path
from .views import hw_home_page_view

urlpatterns = [
    path("hello-world", hw_home_page_view),
]
