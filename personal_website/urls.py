from django.urls import path

from personal_website.views import pw_home_page_view, pw_about_page_view

urlpatterns = [path("home", pw_home_page_view), path("about", pw_about_page_view)]
