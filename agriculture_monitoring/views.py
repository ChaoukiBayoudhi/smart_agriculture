from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Crop,Pest,WeatherData,IrrigationSchedule,SoilMoisture,HarvestLog,Pesticide,CropHealth,CropPestControl
from.serializers import CropSerializer,PestSerializer,weatherDataSerializer,IrrigationScheduleSerializer,SoilMoistureSerializer,HarvestLogSerializer,PesticideSerializer,CropHealthSerializer,CropPestControlSerializer

# CRUD using viewsets.ModelViewSet
#ModelViewwSet is a DRF class that defines the six methods:
 #->create() ==> add an object to the database (HTTTP POST)
 #->destroy() ==> delete an object from the DB (HTTP DELETE)
 #retreive()==>find an object based on its id (HTTP GET)
 #list() ==> returns all objects (HTTP GET)
 #update() ==> updates the object values on the DB (HTTP PUT)
 #partial_update() ==> updates the object values on the DB (partially)(HTTP PATCH)

 #Django ORM methods
 #result=Crop.objects.all() <=> in SQL select * from crop;
 #result=Crop.objects.all()[:5] <=> in SQL select * from crop where rownum<5; (Only the 5th first Crops are returned)
 #result=Crop.objects.filter(name__contains='a') <=> select * from crop where name like '%a%;
 #result=Crop.objects.filter(name__icontains='a') <=> select * from crop where name like '%a% or name like '%A%';
 #Django Lookups:
 #__gt <=> '>'
 #__gte <=> '>='
#__lt <=> '<'
#__lte <=> '<='
# __exact <=> '=='
# __iexact <=> insensitive exact
# __isnull <=> if the field is not initialised
# __first
#__last
#...
#Crop.objects.execlude(plantingDate__year__gt=2020) => get the Crops before 2020
#Crop.objects.all().order_by(name)
#Crop.objects.execlude(plantingDate__year__gt=2020).count()
#HarvestLog.objects.aggregate(quantity__avg)
#...


class CropViewSet(viewsets.ModelViewSet):
    queryset=Crop.objects.all() #as we execute the select * from crop query
    serializer_class=CropSerializer
    #http_method_names=['get','post']
    @action(methods=['GET'],detail=False)
    def get_crops_before(self,request,year):
        crops=Crop.objects.filter(harvestDate__year__lt=year)
        result=CropSerializer(crops,many=True)
        if not crops.exists():
            return Response({'message': f'No Crops before {year}'}, status=status.HTTP_204_NO_CONTENT)
        
        #if not result.data:
           # return Response({'message': f'No Crops before {year}'}, status=status.HTTP_204_NO_CONTENT)
        #or
        #return Respons is not appropriate to use len function directly on result because result is a serializer instance, not a list.
        # Instead, we should check the length of result.data which is the serialized data.
       # if len(result.data) == 0:
         #   return Response({'message': f'No Crops found before {year}'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response(result.data)
    
    #get or delete crops that have a given varity and planted between two given years
    @action(methods=['GET','DELETE'],detail=False)
    def get_or_remove_crops_variety_plating(self,request):
        #get requet params values
        if request.method=='GET':
            variety_name=request.GET.get('varietyName')
            start_y=request.GET.get('start_year')
            end_y=request.GET.get('end_year')
            crops=Crop.objects.filter(variety__iexact=variety_name,plantingDate__year__gte=start_y,plantingDate__year__lte=end_y)
            #or
            #crops=Crop.objects.filter(variety__iexact=variety_name).filter(plantingDate__year__gte=start_y).filter(plantingDate__year__lte=end_y)
            result=CropSerializer(crops,many=True)
            if not result.data:
                return Response({'message': f'No Crops before for that criteria'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(result.data)
        if request.method=='DELETE':
            variety_name=request.DELETE.get('varietyName')
            start_y=request.DELETE.get('start_year')
            end_y=request.DELETE.get('end_year')
            crops=Crop.objects.filter(variety__iexact=variety_name,plantingDate__year__gte=start_y,plantingDate__year__lte=end_y)
            nb_crops=Crop.objects.filter(variety__iexact=variety_name,plantingDate__year__gte=start_y,plantingDate__year__lte=end_y).count()
            
            for x in crops:
                x.delete()
            return Response(f'{nb_crops} have been deleted.')
         


class PestViewSet(viewsets.ModelViewSet):
    queryset=Pest.objects.all()
    serializer_class=PestSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset=WeatherData.objects.all()
    serializer_class=weatherDataSerializer

class IrregationSchedulerViewSet(viewsets.ModelViewSet):
    queryset=IrrigationSchedule.objects.all()
    serializer_class=IrrigationScheduleSerializer

class SoilMoistureViewSet(viewsets.ModelViewSet):
    queryset=SoilMoisture.objects.all()
    serializer_class=SoilMoistureSerializer

class HarvestLogViewSet(viewsets.ModelViewSet):
    queryset=HarvestLog.objects.all()
    serializer_class=HarvestLogSerializer

class PesticideViewSet(viewsets.ModelViewSet):
    queryset=Pesticide.objects.all()
    serializer_class=PesticideSerializer

class CropHealthViewSet(viewsets.ModelViewSet):
    queryset=CropHealth.objects.all()
    serializer_class=CropHealthSerializer

class CropPestControlViewSet(viewsets.ModelViewSet):
    queryset=CropPestControl.objects.all()
    serializer_class=CropPestControlSerializer

