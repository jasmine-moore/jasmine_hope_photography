from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ListUserViewSet, ListPhotoViewSet, ListOriginalViewset, ListWatermarkViewSet, DetailGalleryViewSet, ListClientViewSet

router = DefaultRouter()
router.register('users', ListUserViewSet, basename="users")
router.register('gallery', DetailGalleryViewSet, basename="gallery")
router.register('photo' , ListPhotoViewSet, basename="photo")
router.register('original' , ListOriginalViewset, basename="original")
router.register('watermark', ListWatermarkViewSet, basename="watermark"),
router.register('client', ListClientViewSet, basename="client"),
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('gallery/', ListGallery.as_view()),
#     path('gallery/<int:pk>/', DetailGallery.as_view()),
#     path('photo/', ListPhoto.as_view()),
#     path('photo/<int:pk>/', DetailPhoto.as_view()),
#     path('original/', ListOriginal.as_view()),
#     path('original/<int:pk>/', DetailOriginal.as_view()),
#     path('watermark/', ListWatermark.as_view()),
#     path('watermark/<int:pk>/', DetailWatermark.as_view()),
# ]

