from rest_framework import serializers
from .models import *


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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PriceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSection
        fields = '__all__'


class PriceBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceBlock
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'
