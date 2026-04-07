from django.http import HttpResponse


def hw_home_page_view(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
