from django.db import models
from django_countries.fields import CountryField

class showroom(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    balance = models.IntegerField()
    location = CountryField(default='RU')
    showroom_id =models.IntegerField()
    isActive = models.BooleanField(default=True)


class charact_showroom(models.Model):
    engine_type = models.CharField(max_length=255,null=True)
    max_speed = models.CharField(max_length=255,null=True)
    ammount_of_eng = models.IntegerField()
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    showroom_id =models.IntegerField()
    isActive = models.BooleanField(default=True)

class cars(models.Model):
    engine_type = models.CharField(max_length=255,null=True)
    max_speed = models.CharField(max_length=255,null=True)
    ammount_of_eng = models.IntegerField(default=0)
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    price = models.IntegerField()
    showroom_id =models.IntegerField()
    isActive = models.BooleanField(default=True)

class history(models.Model):
    date = models.DateTimeField()
    buyer = models.CharField(max_length=255)
    price = models.IntegerField()
    showroom_id = models.IntegerField()
    isActive = models.BooleanField(default=True)

class unique_buyers(models.Model):
    buyer_id= models.IntegerField()
    showroom_id = models.IntegerField()
    isActive = models.BooleanField(default=True)



