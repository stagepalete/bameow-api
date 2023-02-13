from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class TokenAuthenticationWithExpiry(TokenAuthentication):

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)

        if token.created < timezone.now() - timedelta(hours=24):
            raise exceptions.AuthenticationFailed('Token has expired')

        return (user, token)

    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
        except exceptions.AuthenticationFailed:
            # Create a new token with expiry date
            user = User.objects.get(auth_token__key=request.auth.key)
            token = Token.objects.create(user=user)
            token.created = timezone.now()
            token.token_expiry = timezone.now() + timedelta(hours=24)
            token.save()

        return (user, token)