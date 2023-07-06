from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookModelViewSet

router = DefaultRouter()
router.register('', BookModelViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
]
