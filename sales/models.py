from django.db import models

class Discount(models.Model):
    from provider.models import Provider
    start = models.DateTimeField()
    end = models.DateTimeField()
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    provider = models.ForeignKey(Provider,models.CASCADE,null=True)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    percent = models.IntegerField(null=True)

class DiscountOfShowrooms(models.Model):
    from showroom.models import Showroom
    start = models.DateTimeField()
    end = models.DateTimeField()
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    showroom = models.ForeignKey(Showroom,models.CASCADE,null=True)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    percent = models.IntegerField(null=True)