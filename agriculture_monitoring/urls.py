from django.urls import path,include
from rest_framework import routers
from .views import CropViewSet
routes=routers.DefaultRouter()
routes.register('crops',CropViewSet,basename='cropviews')
urlpatterns=[
    path('',include(routes.urls)),
]