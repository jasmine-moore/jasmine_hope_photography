from django.urls import path 
from django.views.generic import TemplateView

app_name = 'photo_content'
urlpatterns = [
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about', TemplateView.as_view(template_name="about.hmtl"), name='about'),
    path('gallery/', TemplateView.as_view(template_name="gallery.html"), name='gallery'),
]
