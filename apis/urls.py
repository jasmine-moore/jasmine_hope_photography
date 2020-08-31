from django.urls import path

from .views import ListPhoto, DetailPhoto, ListUser, DetailUser

urlpatterns = [
    path('', ListPhoto.as_view()),
    path('<int:pk>/', DetailPhoto.as_view()),
    path('', ListUser.as_view()),
    path('<int:pk>/', DetailUser.as_view()),
]