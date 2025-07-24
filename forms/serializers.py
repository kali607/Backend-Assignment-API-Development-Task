from rest_framework import serializers
from .models import BogieChecksheetForm, WheelSpecificationForm

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheetForm
        fields = '__all__'

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationForm
        fields = '__all__'
