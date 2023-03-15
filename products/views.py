from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
import rest_framework.permissions as permissions
from . import serializers
from . import models
from . import permissions as customperm

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading, updating profiles'''
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [customperm.isAdminOrReadOnly,]
    search_fields = ('name', 'article',)


