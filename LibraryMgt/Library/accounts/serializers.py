from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'gender', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['gender'], validated_data['password'])
        return user