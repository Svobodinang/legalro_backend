from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import send_email, GeneralInfoViewSet, GarantyViewSet

router = DefaultRouter()
router.register(r'generalInfo', GeneralInfoViewSet)
router.register(r'Garanty', GarantyViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("send_mail", send_email)
]