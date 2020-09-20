# detective/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import send_email, GeneralInfoViewSet

router = DefaultRouter()
router.register(r'generalInfo', GeneralInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("send_mail", send_email)
]