from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    balance = models.IntegerField()
    isActive = models.BooleanField(default=True)

class BuyerHistory(models.Model):
    from showroom.models import Showroom
    buyer = models.ForeignKey(Buyer,models.CASCADE,null=True)
    date = models.DateTimeField()
    price = models.IntegerField()
    showroom = models.ForeignKey(Showroom,models.CASCADE,null=True)
    isActive = models.BooleanField(default=True)

