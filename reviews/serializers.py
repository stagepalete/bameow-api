from rest_framework import serializers
from . import models as review
from profiles.serializers import UserSerializer
from products.serializers import ProductSerializer



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review.reviews
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        response['product'] = ProductSerializer(instance.product).data
        return response