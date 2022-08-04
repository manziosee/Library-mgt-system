from rest_framework import serializers
from rest_framework.response import Response
from .models import Books, Issuebook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuebook
        fields = '__all__'
