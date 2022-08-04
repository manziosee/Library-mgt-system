from django.urls import path
from .views import LibraryEndpoint, BorrowEndpoint
urlpatterns = [
    path('', LibraryEndpoint.as_view()),
    path('getdata/<id>/', LibraryEndpoint.as_view()),
    path('borrow/', BorrowEndpoint.as_view()),
]