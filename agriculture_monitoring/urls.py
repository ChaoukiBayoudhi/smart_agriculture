from django.urls import path,include
from rest_framework import routers
from .views import CropViewSet,PestViewSet,IrregationSchedulerViewSet,WeatherDataViewSet
routes=routers.DefaultRouter()
routes.register('crops',CropViewSet,basename='cropviews')
routes.register('pests',PestViewSet)
routes.register('irrigation/scheduling',IrregationSchedulerViewSet)
routes.register('weather',WeatherDataViewSet)
urlpatterns=[
    path('',include(routes.urls)),
]