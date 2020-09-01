from rest_framework import generics

from photo_content import models
from .serializers import PhotoSerializer, UserSerializer, OriginalPhotoSerializer, WatermarkedPhotoSerializer, GalleriesSerializer

class ListGallery (generics.ListCreateAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = GalleriesSerializer

class DetailGallery (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = GalleriesSerializer

class ListPhoto (generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer

class DetailPhoto (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer

class ListOriginal (generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = OriginalPhotoSerializer

class DetailOriginal (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = OriginalPhotoSerializer

class ListWatermark (generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = WatermarkedPhotoSerializer

class DetailWatermark (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = WatermarkedPhotoSerializer

class ListUser (generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class =  UserSerializer

class DetailUser (generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

