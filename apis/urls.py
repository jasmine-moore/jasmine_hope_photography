from django.urls import path

from .views import ListPhoto, DetailPhoto, ListOriginal, DetailOriginal, ListWatermark, DetailWatermark, ListUser, DetailUser, ListGallery , DetailGallery

urlpatterns = [
    path('gallery/', ListGallery.as_view()),
    path('gallery/<int:pk>/', DetailGallery.as_view()),
    path('photo/', ListPhoto.as_view()),
    path('photo/<int:pk>/', DetailPhoto.as_view()),
    path('original/', ListOriginal.as_view()),
    path('original/<int:pk>/', DetailOriginal.as_view()),
    path('watermark/', ListWatermark.as_view()),
    path('watermark/<int:pk>/', DetailWatermark.as_view()),
    path('user/', ListUser.as_view()),
    path('user/<int:pk>/', DetailUser.as_view()),
]