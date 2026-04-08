from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in (settings.LOGIN_URL, settings.SIGNUP_URL):
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return self.get_response(request)
