from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class ProviderAPIViewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    ammountOfBuyers = serializers.IntegerField()
    providerId = serializers.IntegerField()

class ListOfCarsAPIViewSerializer(serializers.Serializer):
    class Meta:
        model=listOfCars
        fields =('id',"engine_type","max_speed","ammount_of_eng","model","mark","price","providerId",)
