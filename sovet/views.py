from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import GeneralInfoSerializer
from .models import GeneralInfo

@api_view(['POST'])
def send_email(request):
    recipients = ['info@sovetpravo.ru']
    message = u'Имя: ' + request.data['name'] + \
        u'\nТелефон: ' + request.data['tel']
    send_mail(u'Запрос на звонок с сайта', message, 'detective.moscow@bk.ru', recipients)
    return HttpResponse('ok')

class GeneralInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralInfoSerializer
    queryset = GeneralInfo.objects.all()
