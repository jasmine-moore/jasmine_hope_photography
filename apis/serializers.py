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

class ClientSerializer (serializers.ModelSerializer): 
    class Meta:
        model = models.Photo
        fields = (
            'original_photo',
            'client_name',
            'photographer',

        )
 

class OriginalPhotoSerializer (serializers.ModelSerializer):
    client_info = ClientSerializer(many=True, read_only=True)
    class Meta:
        model = models.Photo
        fields = (
            'original_photo', 
            'id',
            'gallery', 
            'photo_date', 
            'client_name',
            'client_info',
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
            'user',
            'name',
            'date', 
            'photographer',
            'photo_set',
            'description',
        )

class UserSerializer (serializers.ModelSerializer): 
    client_set = OriginalPhotoSerializer(read_only=True, many=True, source='original_photo')
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