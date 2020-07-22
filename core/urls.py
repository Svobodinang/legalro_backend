# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import send_email, GeneralInfoViewSet, RunTitleViewSet, GarantyViewSet, BenefitViewSet, ServicesViewSet

router = DefaultRouter()
router.register(r'generalInfo', GeneralInfoViewSet)
router.register(r'runTitles', RunTitleViewSet)
router.register(r'garanties', GarantyViewSet)
router.register(r'benefits', BenefitViewSet)
router.register(r'services', ServicesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("send_mail", send_email)
]