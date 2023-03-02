from rest_framework import serializers
from . import models
from . import permissions
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'article', 'color', 'size', 'rating', 'price', 'description')
    
    def create(self, validated_data):
        product = models.Product(
            name = validated_data['name'],
            article = validated_data['article'],
            color = validated_data['color'],
            size = validated_data['size'],
            rating = validated_data['rating'],
            price = validated_data['price'],
            description = validated_data['description']
        )
        product.save()
        return product
        