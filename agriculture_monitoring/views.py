from django.shortcuts import render
from rest_framework import viewsets
from .models import Crop
from.serializers import CropSerializer

# CRUD using viewsets.ModelViewSet
#ModelViewwSet is a DRF class that defines the six methods:
 #->create() ==> add an object to the database (HTTTP POST)
 #->destroy() ==> delete an object from the DB (HTTP DELETE)
 #retreive()==>find an object based on its id (HTTP GET)
 #list() ==> returns all objects (HTTP GET)
 #update() ==> updates the object values on the DB (HTTP PUT)
 #partial_update() ==> updates the object values on the DB (partially)(HTTP PATCH)
class CropViewSet(viewsets.ModelViewSet):
    queryset=Crop.objects.all() #as we execute the select * from crop query
    serializer_class=CropSerializer
    #http_method_names=['get','post']