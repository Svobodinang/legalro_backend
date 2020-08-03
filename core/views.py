# from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import GeneralInfoSerializer, RunTitleSerializer, GarantySerializer, BenefitSerializer, ServicesSerializer
from .models import GeneralInfo, RunTitle, Garanty, Benefit, Services


@api_view(['POST'])
def send_email(request):
    recipients = ['detective.moscow@bk.ru']
    print(request.data)
    message = 'Имя: ' + request.data['name'] + \
        '\nТелефон: ' + request.data['tel']
    send_mail('Запрос на звонок с сайта', message, 'detective.moscow@bk.ru', recipients)
    return HttpResponse('ok')


class GeneralInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralInfoSerializer
    queryset = GeneralInfo.objects.all()


class RunTitleViewSet(viewsets.ModelViewSet):
    serializer_class = RunTitleSerializer
    queryset = RunTitle.objects.all()


class GarantyViewSet(viewsets.ModelViewSet):
    serializer_class = GarantySerializer
    queryset = Garanty.objects.all()


class BenefitViewSet(viewsets.ModelViewSet):
    serializer_class = BenefitSerializer
    queryset = Benefit.objects.all()


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
