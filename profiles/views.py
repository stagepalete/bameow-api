from rest_framework import viewsets, filters, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.contrib.auth import authenticate

from . import serializers
from . import models
from . import permissions

class UserViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading, updating profiles'''
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.UpdateOwnProfile, permissions.IsNotAuthenticated )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name', 'lastname',)



class LoginViewSet(viewsets.ViewSet):
    # '''Checks email and passwords and return authtoken'''
    # serializer_class = AuthTokenSerializer
    # def create(self, request):
    #     '''Use the ObtainAuthToken APIView to validate and create token'''
    #     return ObtainAuthToken().as_view()(request=request._request)
    '''Checks email and passwords and return authtoken'''
    serializer_class = AuthTokenSerializer
    def create(self, request):
        '''Use the ObtainAuthToken APIView to validate and create token'''
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)

        # Set the user's Token_expiry
        expiry = datetime.now() + timedelta(days=7)
        user.Token_expiry = expiry
        user.save()

        return Response({'token': token.key})

class TokenIssuerViewSet(viewsets.ViewSet):
    def issue_token(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)

        # Set the token's expiration date
        expiry = datetime.now() + timedelta(days=7)
        user.token_expiry = expiry
        user.save()

        return Response({'token': token.key})