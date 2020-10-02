from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import send_email, GeneralInfoViewSet, GarantyViewSet, GoalsViewSet, DocsViewSet

router = DefaultRouter()
router.register(r'generalInfo', GeneralInfoViewSet)
router.register(r'Garanty', GarantyViewSet)
router.register(r'Goals', GoalsViewSet)
router.register(r'Docs', DocsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("send_mail", send_email)
]