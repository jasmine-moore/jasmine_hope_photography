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

class OriginalPhotoSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = (
            'original_photo', 
            'id',
            'gallery', 
            'photo_date', 
            'client_name',
            'photographer',
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
            'name',
            'date', 
            'photographer',
            'photo_set',
        )

class UserSerializer (serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email',  
            'is_staff',
            'is_superuser', 
            'last_login', 
            'date_joined',
        )