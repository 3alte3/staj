from django.db import models

class offers(models.Model):
    buyerId = models.CharField(max_length=255)
    maxPrice = models.IntegerField()
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    