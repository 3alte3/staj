from django.db import models

class buyer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    buyerId = models.CharField(max_length=255)
    balance = models.IntegerField()
    isActive = models.BooleanField(default=True)

class buyer_history(models.Model):
    buyerId = models.CharField(max_length=255)
    date = models.DateTimeField()
    price = models.IntegerField()
    showroom_id = models.IntegerField()
    isActive = models.BooleanField(default=True)

