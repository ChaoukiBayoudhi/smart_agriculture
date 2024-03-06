from django.db import models
class MapLocalisation(models.Model):
    longitude = models.DecimalField(max_digits=9,decimal_places=6)
    latitude = models.DecimalField(max_digits=8,decimal_places=6)
    class Meta:
        #this model is abstract, it will not be created in the database
        #it'll be used only on inheritance relationship
        abstract = True

class Crop(MapLocalisation):
    name = models.CharField(max_length=100)
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

