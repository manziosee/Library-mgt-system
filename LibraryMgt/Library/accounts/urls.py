from django.urls import path
from .views import * 
from knox import views as knox_views

urlpatterns = [
    path('', SignUp.as_view()),
    path('login/', LogIn.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]