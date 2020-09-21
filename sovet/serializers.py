from rest_framework import serializers
from .models import GeneralInfo, Garanty

class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'

class GarantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Garanty
        fields = '__all__'