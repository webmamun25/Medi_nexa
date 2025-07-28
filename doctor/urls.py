from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet,SpecializationViewSet,DesignationViewSet,AvailabletimeViewSet,RatingsViewSet,SmartDoctorSearchAPIView
router = DefaultRouter()

router.register('list', DoctorViewSet)
router.register('specialization', SpecializationViewSet)
router.register('designation', DesignationViewSet)
router.register('available_time', AvailabletimeViewSet)
router.register('ratings', RatingsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('smart-search/', SmartDoctorSearchAPIView.as_view(), name='smart-doctor-search'),

]