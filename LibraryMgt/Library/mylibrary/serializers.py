from rest_framework import serializers
from rest_framework.response import Response
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
