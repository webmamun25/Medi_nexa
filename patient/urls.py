from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,Registrationview, VerifyEmailView,LoginView,LogoutView
router = DefaultRouter()
router.register('list', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', Registrationview.as_view(),name="registration"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify-email'),
]