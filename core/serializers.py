from rest_framework import serializers
from .models import GeneralInfo, RunTitle, Garanty, Benefit, Services

class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'

class RunTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTitle
        fields = '__all__'

class GarantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Garanty
        fields = '__all__'

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'