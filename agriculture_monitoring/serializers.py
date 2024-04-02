from .models import Crop,Pest
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

