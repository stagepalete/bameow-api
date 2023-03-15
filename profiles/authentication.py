# from datetime import timedelta
# from django.contrib.auth.models import User
# from django.utils import timezone
# from rest_framework import authentication, exceptions
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication

# class TokenAuthenticationWithExpiry(TokenAuthentication):

#     def authenticate_credentials(self, key):
#         user, token = super().authenticate_credentials(key)

#         if token.created < timezone.now() - timedelta(hours=24):
#             raise exceptions.AuthenticationFailed('Token has expired')

#         return (user, token)

#     def authenticate(self, request):
#         try:
#             user, token = super().authenticate(request)
#             return (user, token)
#         except exceptions.AuthenticationFailed:
#             auth = authentication.get_authorization_header(request).split()
#             if not auth or auth[0].lower() != b'token':
#                 raise exceptions.AuthenticationFailed('No token provided')
#             if len(auth) == 1:
#                 raise exceptions.AuthenticationFailed('Invalid token header. No credentials provided.')
#             if len(auth) > 2:
#                 raise exceptions.AuthenticationFailed('Invalid token header. Token string should not contain spaces.')
#             try:
#                 token = auth[1].decode()
#             except UnicodeError:
#                 raise exceptions.AuthenticationFailed('Invalid token header. Token string should not contain invalid characters.')
#             return self.authenticate_credentials(token)


from datetime import timedelta
from django.utils import timezone
from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from . import models

class TokenAuthenticationWithExpiry(TokenAuthentication):

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)

        if token.created < timezone.now() - timedelta(hours=0.01):
            raise exceptions.AuthenticationFailed('Token has expired')

        return (user, token)

    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
        except TypeError:
            raise exceptions.AuthenticationFailed('Invalid token')

        if token.created < timezone.now() - timedelta(hours=0.01):
            raise exceptions.AuthenticationFailed('Token has expired')

        return (user, token)
