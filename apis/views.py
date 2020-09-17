from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User

from photo_content.models import Gallery, Photo
from .serializers import PhotoSerializer, UserSerializer, OriginalPhotoSerializer, WatermarkedPhotoSerializer, GalleriesSerializer, ClientSerializer
from .permissions import is_owner, readonly, isadminorreadonly
# class ListGallery (generics.ListCreateAPIView):
#     queryset = models.Gallery.objects.all()
#     serializer_class = GalleriesSerializer

# class DetailGallery (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Gallery.objects.all()
#     serializer_class = GalleriesSerializer

class DetailGalleryViewSet (viewsets.ModelViewSet):
    serializer_class = GalleriesSerializer
    queryset = Gallery.objects.all()
    permission_classes = [isadminorreadonly]
    

# class ListPhoto (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = PhotoSerializer

# class DetailPhoto (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = PhotoSerializer

class ListPhotoViewSet (viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [is_owner, permissions.IsAuthenticated]
    

# class ListOriginal (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = OriginalPhotoSerializer

# class DetailOriginal (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = OriginalPhotoSerializer

class ListOriginalViewset (viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = OriginalPhotoSerializer
    permission_classes = [is_owner, permissions.IsAuthenticated]

# class ListWatermark (generics.ListCreateAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = WatermarkedPhotoSerializer

# class DetailWatermark (generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Photo.objects.all()
#     serializer_class = WatermarkedPhotoSerializer

class ListWatermarkViewSet (viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = WatermarkedPhotoSerializer
    permission_classes = [readonly]

# class ListUser (generics.ListCreateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class =  UserSerializer

# class DetailUser (generics.RetrieveUpdateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer

class ListUserViewSet (viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [isadminorreadonly]

class ListClientViewSet (viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = User.objects.all()
    permission_classes = [isadminorreadonly]
    

    def get_object(self): 
        return self.request.user


