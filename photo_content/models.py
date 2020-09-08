from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    photographer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class Photo(models.Model): 
    original_photo = models.ImageField(upload_to='images/original/')
    watermarked_photo = models.ImageField(upload_to='images/watermarked/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo_date = models.DateTimeField()
    client_name = models.ForeignKey(User, on_delete=models.CASCADE)
    photographer = models.CharField(max_length=200)

    