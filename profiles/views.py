from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from profiles.authentication import TokenAuthenticationWithExpiry

from . import serializers
from . import models
from . import permissions

class UserViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading, updating profiles'''
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.UpdateOwnProfile, permissions.IsAuthenticated )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name', 'lastname',)



class LoginViewSet(viewsets.ViewSet):
    '''Checks email and passwords and return authtoken'''
    serializer_class = AuthTokenSerializer
    def create(self, request):
        '''Use the ObtainAuthToken APIView to validate and create token'''
        return ObtainAuthToken().as_view()(request=request._request)