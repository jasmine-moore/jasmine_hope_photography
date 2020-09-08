from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('createaccount/', views.SignUpView.as_view(), name='createaccount'),
    path('<str:username>/', views.UserProfileView.as_view(), name= 'profile'),
]