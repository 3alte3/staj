from django.db import models

class provider(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    ammountOfBuyers = models.IntegerField()
    providerId = models.IntegerField()
    isActive = models.BooleanField(default=True)

class listOfCars(models.Model):
    engine_type = models.CharField(max_length=255,null=True)
    max_speed = models.CharField(max_length=255,null=True)
    ammount_of_eng = models.IntegerField(default=0)
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    price = models.IntegerField()
    providerId = models.IntegerField()
    isActive = models.BooleanField(default=True)
