from django.urls import path 
from django.views.generic import TemplateView

app_name = 'photo_content'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('gallery/', TemplateView.as_view(template_name="gallery.html"), name='gallery'),
]
