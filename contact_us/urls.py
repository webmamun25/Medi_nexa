from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactusViewSet
router = DefaultRouter()
router.register('', ContactusViewSet)

urlpatterns = [
    path('', include(router.urls))
]