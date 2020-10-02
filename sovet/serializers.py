from rest_framework import serializers
from .models import GeneralInfo, Garanty, Goals,  Docs, ServiceBlock, ServiceSection


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'


class GarantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Garanty
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = '__all__'

class ServiceBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBlock
        fields = '__all__'


class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = '__all__'