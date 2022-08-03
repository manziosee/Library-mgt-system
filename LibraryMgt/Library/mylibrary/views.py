from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Books
# Create your views here.

class LibraryEndpoint(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


    def put(self, request, id=None):
        queryset = Books.objects.get(id=id)
        serializer = BookSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        query = Books.objects.get(id=id)
        query.delete()
        return Response('Book deleted successfully')
    

