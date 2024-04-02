from django.db import models
class MapLocalisation(models.Model):
    longitude = models.DecimalField(max_digits=9,decimal_places=6)
    latitude = models.DecimalField(max_digits=8,decimal_places=6)
    class Meta:
        #this model is abstract, it will not be created in the database
        #it'll be used only on inheritance relationship
        abstract = True

class Crop(MapLocalisation):
    name = models.CharField(max_length=100, unique=True)
    variety =models.CharField(max_length=100)
    plantingDate = models.DateField(auto_now_add=True)
    expectedHarvestDate = models.DateField(null=True,blank=True)
    harvestDate = models.DateField()
    image=models.ImageField(upload_to='crops_images/',null=True,blank=True)
    #the class Meta is an inner class that is used to define metadata on models, Serializers, Forms, 
    #this class must be just after the fields of the model
    #in this class we can define some properties of the model
    #like the ordering of records on the database table
    class Meta:
        ordering = ['name','plantingDate']#ordering the records by name and planting date in the ascending order
        #ordering=['-name']#ordering the records by name in the descending order
        db_table = 'crops' #this is the name of the table in the database
        verbose_name='Crop monitoring' #this is the name of the model in the admin site
        verbose_name_plural='Crops monitoring' #this is the name of the list of records in the admin site
        unique_together = ['name','plantingDate'] #this is to define that the combination of name and planting date must be unique
        constraints = [
            models.CheckConstraint(check=models.Q(expectedHarvestDate__gte=models.F('plantingDate')),name='expectedHarvestDate_gte_plantingDate'),
            models.CheckConstraint(check=models.Q(harvestDate__gte=models.F('plantingDate')),name='harvestDate_gte_plantingDate'),
            models.CheckConstraint(check=models.Q(harvestDate__gte=models.F('expectedHarvestDate')),name='harvestDate_gte_expectedHarvestDate'),
        ]
        #we can define index on the module using the property indexes
        indexes = [
           models.Index(fields=['name','plantingDate']),
        ]
    def __str__(self) -> str:
        #return f'{self.name} - {self.plantingDate.year}'
        #return self.name,' - ',self.plantingDate.year.year
        return '%s - %d'%(self.name,self.plantingDate.year)
    
class WeatherData(MapLocalisation):
    timestamp=models.DateTimeField()
    temperature=models.FloatField(default=0)
    humidity =models.FloatField(default=0)
    precipitation =models.FloatField(default=0)
    wind_speed=models.FloatField()
    #relationship between WeatherData and Crop (n-1)
    crop=models.ForeignKey(Crop,on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        db_table='weather_data'

class IrrigationSchedule(models.Model):
    schedule=models.TextField()
    duration=models.DurationField()
    #relationship between IrrigationSchedule and Crop (1-1)
    crop=models.OneToOneField(Crop,on_delete=models.CASCADE)
    class Meta:
        db_table='irrigation_schedule'
    def __str__(self):
        return "id = ",self.id
        
class HealthStatus(models.TextChoices):
    Healthy='HLTY','healthy crop'
    Stressed='STSD','stressed crop'
    Deseased='DSED','deseased crop'

class CropHealth(models.Model):
    timestamp=models.DateTimeField()
    health_status=models.CharField(max_length=20,choices=HealthStatus.choices,default=HealthStatus.Healthy)
    #health_status=models.CharField(max_length=50, choices=[('Healthy','healthy crop'),('Stressed','stressed crop'),('Deseased','deseased crop')],default='Healthy')
    recommandations=models.TextField()
    crop=models.OneToOneField(Crop, on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        db_table='crop_health'
    def __str__(self):
        return self.health_status
    
class Pest(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='pests_images/',null=True,blank=True)
    #Many to many relationship between Pest and Crop (n-n)
    crops=models.ManyToManyField(Crop,through='CropPestControl',through_fields=('pest','crop'))
    class Meta:
        db_table='pests'
    def __str__(self):
        return self.name

class CropPestControl(models.Model):
    crop=models.ForeignKey(Crop,on_delete=models.CASCADE)
    pest=models.ForeignKey(Pest,on_delete=models.CASCADE)
    control_date=models.DateField()
    control_measures=models.TextField()
    class Meta:
        db_table='crop_pest_control'

    def __str__(self):
        return f'{self.crop.name} - {self.pest.name} - {self.control_date}'


