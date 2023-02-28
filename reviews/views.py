from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import permissions

from . import serializers
from . import models


class ReviewViewSet(viewsets.ModelViewSet):
    '''Reviews view'''
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.reviews.objects.all()
    
