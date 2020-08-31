from django.urls import path 
from django.views.generic import TemplateView

from . import TempalateView 

app_name = 'photo_content'
urlpatterns = [
    path('', TempalateView.as_view(template_name="home.html"), name='home')
]
