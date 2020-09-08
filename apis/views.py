from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from photo_content.models import Gallery, Photo
from .serializers import PhotoSerializer, UserSerializer, OriginalPhotoSerializer, WatermarkedPhotoSerializer, GalleriesSerializer, ClientSerializer

# class ListGallery (generics.ListCreateAPIView):
#     queryset = models.Gallery.objects.all()
#     serializer_class = GalleriesSerializer

# class DetailGallery (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Gallery.objects.all()
#     serializer_class = GalleriesSerializer

class DetailGalleryViewSet (viewsets.ModelViewSet):
    serializer_class = GalleriesSerializer
    queryset = Gallery.objects.all()

# class ListPhoto (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = PhotoSerializer

# class DetailPhoto (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = PhotoSerializer

class ListPhotoViewSet (viewsets.ModelViewSet):
    serializer_class = Photo.objects.all()
    queryset = PhotoSerializer

# class ListOriginal (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = OriginalPhotoSerializer

# class DetailOriginal (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = OriginalPhotoSerializer

class ListOriginalViewset (viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = OriginalPhotoSerializer

# class ListWatermark (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = WatermarkedPhotoSerializer

# class DetailWatermark (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = WatermarkedPhotoSerializer

class ListWatermarkViewSet (viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = WatermarkedPhotoSerializer

# class ListUser (generics.ListCreateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class =  UserSerializer

# class DetailUser (generics.RetrieveUpdateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer

class ListUserViewSet (viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ListClientViewSet (viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = User.objects.all()

    def get_object(self): 
        return self.request.user

