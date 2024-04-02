from django.shortcuts import render
from rest_framework import viewsets
from .models import Crop
from.serializers import CropSerializer

# CRUD using viewsets.ModelViewSet
class CropViewSet(viewsets.ModelViewSet):
    queryset=Crop.objects.all() #as we execute the select * from crop query
    serializer_class=CropSerializer
    #http_method_names=['get','post']