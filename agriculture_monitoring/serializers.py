from .models import Crop,Pest,WeatherData,IrrigationSchedule,SoilMoisture,HarvestLog,Pesticide,CropHealth,CropPestControl
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

class SoilMoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model=SoilMoisture
        fields='__all__'

class HarvestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=HarvestLog
        fields='__all__'

class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pesticide
        fields='__all__'

class CropHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model=CropHealth
        fields='__all__'

class CropPestControlSerializer(serializers.ModelSerializer):
    class Meta:
        model=CropPestControl
        fields='__all__'



