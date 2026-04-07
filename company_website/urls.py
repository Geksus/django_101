from django.urls import path
from .views import cw_home_page_view, AboutPageView

urlpatterns = [
    path("c-home", cw_home_page_view, name="cw_home_page"),
    path("c-about", AboutPageView.as_view(), name="cw_about_page"),
]
