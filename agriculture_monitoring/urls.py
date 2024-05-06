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
    path('cropsbefore/<int:year>',CropViewSet.as_view({'get':'get_crops_before'})),
    path('crops-varity-planting/',CropViewSet.as_view({'get':'get_or_remove_crops_variety_plating','delete':'get_or_remove_crops_variety_plating'}))
]