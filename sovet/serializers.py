from rest_framework import serializers
from .models import GeneralInfo, Garanty, Goals,  Docs

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