from rest_framework import serializers
from photo_content import models
from django.contrib.auth.models import User

class PhotoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Photo
        fields = (
            'original_photo', 
            'watermarked_photo',
            'id',
            'gallery', 
            'photo_date', 
            'client_name',
            'photographer',
        )

# class ClientSerializer (serializers.ModelSerializer): 
#     class Meta:
#         model = models.Photo
#         fields = (
#             'client_name',
#         )
 

class OriginalPhotoSerializer (serializers.ModelSerializer):
    # client_info = ClientSerializer(read_only=True, source='client_name')
    class Meta:
        model = models.Photo
        fields = (
            'original_photo', 
            'id',
            'gallery', 
            'photo_date', 
            'client_name',
            # 'client_info',
            'photographer',
        )
    
class NestedOriginalPhotoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Photo
        fields = (
            'original_photo', 
            'id', 
            'gallery',
            'photo_date',
        )

class WatermarkedPhotoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Photo
        fields = ( 
            'watermarked_photo',
            'id',
            'gallery', 
            'photo_date', 
            'client_name',
            'photographer',
        )

class NestedWatermarkedPhotoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Photo
        fields = ( 
            'watermarked_photo',
            'id',
            'photo_date', 
        )

class GalleriesSerializer (serializers.ModelSerializer): 
    photo_set = NestedWatermarkedPhotoSerializer(read_only=True, many=True)
    class Meta: 
        model = models.Gallery
        fields = (
            'id',
            'user',
            'name',
            'date', 
            'photographer',
            'photo_set',
            'description',
        )

class NestedGalleriesSerializer (serializers.ModelSerializer): 
    photo_set = NestedOriginalPhotoSerializer(read_only=True, many=True)
    class Meta: 
        model = models.Gallery
        fields = (
            'id',
            'name',
            'date', 
            'photographer',
            'photo_set',
            'description',
        )


class UserSerializer (serializers.ModelSerializer): 
    client_set = NestedOriginalPhotoSerializer(read_only=True, many=True, source='photo_set')
    class Meta:
        model = models.User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email',  
            'is_staff',
            'is_superuser', 
            'last_login', 
            'date_joined',
            'client_set',
        )

class ClientSerializer (serializers.ModelSerializer): 
    client_set = NestedGalleriesSerializer(read_only=True, many=True, source='gallery_set')
    class Meta:
        model = models.User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email',  
            'is_staff',
            'is_superuser', 
            'last_login', 
            'date_joined',
            'client_set',
        )

