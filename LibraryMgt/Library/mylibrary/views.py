from django.shortcuts import render
from .serializers import BookSerializer, IssueSerializer
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

    def get(self, request, id=None):
        if id:
            try:
                query=Books.objects.get(id=id)
                serializer = BookSerializer(query, many=False)
                return Response(serializer.data)
            except Books.DoesNotExist:
                return Response({'Message':"The Book doesn't exist!!"})
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


    def put(self, request, id):
        queryset = Books.objects.get(id=id)
        serializer = BookSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        query = Books.objects.get(id=id)
        query.delete()
        return Response('Book deleted successfully')

class BorrowEndpoint(APIView):
    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

