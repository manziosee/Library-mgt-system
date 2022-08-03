from django.urls import path
from .views import LibraryEndpoint
urlpatterns = [
    path('', LibraryEndpoint.as_view()),
    path('updatedata/<id>/', LibraryEndpoint.as_view()),
]