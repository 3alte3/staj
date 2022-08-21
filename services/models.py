from django.db import models

class Offers(models.Model):
    from buyer.models import Buyer
    buyer = models.ForeignKey(Buyer,models.CASCADE,null=True)
    maxPrice = models.IntegerField()
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

class Statistics(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(null=True)

    