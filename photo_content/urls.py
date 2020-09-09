from django.urls import path 
from django.views.generic import TemplateView

app_name = 'photo_content'
urlpatterns = [
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('userprofile/', TemplateView.as_view(template_name="userprofile.html"), name='profile'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('gallery/', TemplateView.as_view(template_name="gallery.html"), name='gallery'),
]
