from .models import Crop,Pest,WeatherData,IrrigationSchedule
from rest_framework import serializers
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields='__all__'
        #fields=['name','variety','harvestDate']
class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pest
        fields='__all__'

class weatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeatherData
        fields='__all__'

class IrrigationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=IrrigationSchedule
        fields='__all__'

