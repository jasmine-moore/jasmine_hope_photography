from rest_framework import serializers
from photo_content import models
from django.contrib.auth.models import User

class PhotoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Photo
        fields = (
            'original_photo', 
            'watermarked_photo',
            'gallery', 
            'photo_date', 
            'client_name',
            'photographer',
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