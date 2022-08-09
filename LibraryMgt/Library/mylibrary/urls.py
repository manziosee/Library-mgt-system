from django.urls import path
from .views import LibraryEndpoint, create, update
urlpatterns = [
    path('', LibraryEndpoint.as_view()),
    path('getdata/<id>/', LibraryEndpoint.as_view()),
    path('borrow/', create.as_view()),
    path('borrowdata/<pk>/', update.as_view()),
]