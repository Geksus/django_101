from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime


def get_age(birth_year):
    return datetime.now().year - int(birth_year)


def pw_home_page_view(request):
    return HttpResponse("<h1>Homepage</h1>")


def pw_about_page_view(request):
    context = {"name": "Alex", "age": get_age(1984)}
    return render(request, "pw_about.html", context=context)
