from rest_framework import serializers
from . import models

class AdminOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = '__all__'
    def create(self, validated_data):
        order = models.Orders(
            product = validated_data['product'],
            user = validated_data['user'],
            status = validated_data['status'],
            quant = validated_data['quant'],
            country = validated_data['country'],
            district = validated_data['district'],
            city = validated_data['city'],
            street = validated_data['street'],
            house = validated_data['house'],
            appartment = validated_data['appartment'],
        )
        order.save()
        return order
    def to_representation(self, instance):
        return super().to_representation(instance)


class UserOrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = models.Orders
        fields = ['product', 'user', 'quant', 'country', 'district', 'city', 'street', 'house', 'appartment']
    
    def create(self, validated_data):
        user = self.context['request'].user
        order = models.Orders(
            product=validated_data['product'],
            user=user,
            quant=validated_data['quant'],
            country=validated_data['country'],
            district=validated_data['district'],
            city=validated_data['city'],
            street=validated_data['street'],
            house=validated_data['house'],
            appartment=validated_data['appartment'],
        )
        order.save()
        return order
