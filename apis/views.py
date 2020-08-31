from rest_framework import generics

from photo_content import models
from .serializers import PhotoSerializer, UserSerializer

class ListPhoto (generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer

class DetailPhoto (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer

class ListUser (generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class =  UserSerializer

class DetailUser (generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

