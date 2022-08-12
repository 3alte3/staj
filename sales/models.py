from django.db import models

class discount(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    model = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    showroom_id = models.IntegerField(null=True)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    percent = models.IntegerField(null=True)

