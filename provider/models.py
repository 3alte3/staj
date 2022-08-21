from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    ammountOfBuyers = models.IntegerField()
    isActive = models.BooleanField(default=True)

class ListOfCars(models.Model):
    engine_type = models.CharField(max_length=255,null=True)
    max_speed = models.CharField(max_length=255,null=True)
    ammount_of_eng = models.IntegerField(default=0)
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    price = models.IntegerField()
    provider = models.ForeignKey(Provider,models.CASCADE,null=True)
    isActive = models.BooleanField(default=True)

class ProviderHistory(models.Model):
    from showroom.models import Showroom
    date = models.DateTimeField()
    provider = models.ForeignKey(Provider,models.CASCADE,null=True)
    showroom = models.ForeignKey(Showroom,models.CASCADE,null=True)
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)


