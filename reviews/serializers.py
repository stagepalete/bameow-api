from rest_framework import serializers
from . import models as review


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data
    
class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        model = review.reviews
        fields = ['user','comment','image', 'helpfull', 'date', 'children']
