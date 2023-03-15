from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'email', 'name','lastname', 'region','password')
        extra_kwargs = {'password': {'write_only': True} }

    def create(self, validated_data):
        user = models.User(
            email = validated_data['email'],
            name = validated_data['name'],
            region = validated_data['region'],
            lastname = validated_data['lastname'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user