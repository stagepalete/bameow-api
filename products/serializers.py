from rest_framework import serializers
from . import models
from reviews.serializers import ReviewSerializer
from profiles.serializers import UserSerializer
class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'article', 'color', 'size', 'rating', 'price', 'description','reviews')
        # fields = '__all__'
        # exclude = ('draft', )
    def create(self, validated_data):
        product = models.Product(
            name = validated_data['name'],
            article = validated_data['article'],
            color = validated_data['color'],
            size = validated_data['size'],
            rating = validated_data['rating'],
            price = validated_data['price'],        
            description = validated_data['description'],
        )
        product.save()
        return product

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['reviews'] = ReviewSerializer(instance.reviews).data
    #     # response['reviews'][0]['user'] = UserSerializer(instance.user).data
    #     return response

        