from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as knoxLoginView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterUser , UserSerializer
from django.contrib.auth import get_user_model, login
User = get_user_model()
# Create your views here.

# class SignUp(APIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = RegisterUser(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         userr =  serializer.save()
#         return Response({
#             "user": UserSerializer(userr, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(userr)[1]
#         })
    
#     def get(self, request):
#         query = User.objects.all()
#         serializer =  UserSerializer(query, many=True)
#         return Response(serializer.data)

class SignUp(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response(serializer.data)

    def get(self, request):
        query = User.objects.all()
        serializer =  UserSerializer(query, many=True)
        return Response(serializer.data)
        
# class LogIn(knoxLoginView):
#     permission_classes = [AllowAny]
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LogIn, self).post(request, format=None)


    

    