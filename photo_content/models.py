from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Photo(models.Model): 
    original_photo = models.ImageField(upload_to='images/original/')
    watermarked_photo = models.ImageField(upload_to='images/watermarked/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo_date = models.DateTimeField()
    client_name = models.CharField(max_length=200)
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)