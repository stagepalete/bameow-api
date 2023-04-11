from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
import rest_framework.permissions as permissions
from .permissions import CheckOwnOrders 
from . import serializers
from . import models


class AdminOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AdminOrderSerializer
    queryset = models.Orders.objects.all()
    filter_backends = (filters.SearchFilter,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    search_fields = ('user')
    
class UserOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserOrderSerializer
    filter_backends = (filters.SearchFilter,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, CheckOwnOrders]
    search_fields = ('product')

    def get_queryset(self):
        user = self.request.user
        return models.Orders.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
