from datetime import datetime, timedelta
from django.contrib.auth import get_user
from rest_framework import exceptions

class TokenExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = get_user(request)

        if user and user.token_expiry:
            expiry = datetime.strptime(user.token_expiry, '%Y-%m-%d %H:%M:%S.%f')

            if expiry < datetime.now():
                raise exceptions.AuthenticationFailed('Token has expired')

        response = self.get_response(request)

        return response
