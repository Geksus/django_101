from django.urls import path

from personal_website.views import pw_home_page_view, pw_about_page_view

urlpatterns = [path("p-home", pw_home_page_view, name="p_home"), path("p-about", pw_about_page_view, name="pw_about")]
