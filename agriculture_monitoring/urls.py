from django.urls import path,include
from rest_framework import routers
from .views import CropViewSet,PestViewSet,IrregationSchedulerViewSet,WeatherDataViewSet,PesticideViewSet,CropHealthViewSet,SoilMoistureViewSet,HarvestLogViewSet,CropPestControlViewSet
routes=routers.DefaultRouter()
routes.register('crops',CropViewSet,basename='cropviews')
routes.register('pests',PestViewSet)
routes.register('irrigation/scheduling',IrregationSchedulerViewSet)
routes.register('weather',WeatherDataViewSet)
routes.register('pesticides',PesticideViewSet)
routes.register('crophealth',CropHealthViewSet)
routes.register('soilmoisture',SoilMoistureViewSet)
routes.register('harvestlog',HarvestLogViewSet)
routes.register('croppestcontrol',CropPestControlViewSet)
urlpatterns=[
    path('',include(routes.urls)),
]