from django.contrib import admin

from .models import Crop,WeatherData,Pest,CropPestControl,CropHealth, IrrigationSchedule

# Register your models here.
admin.site.register(Crop)
admin.site.register(WeatherData)
admin.site.register(Pest)
admin.site.register(CropPestControl)
admin.site.register(CropHealth)
admin.site.register(IrrigationSchedule)
