from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class ProviderAPIViewSerializer(serializers.ModelSerializer):
    class Meta :
        model = provider
        fields = ("name","date","ammountOfBuyers","providerId",)


class ListOfCarsAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=listOfCars
        fields =('id',"engine_type","max_speed","ammount_of_eng","model","mark","price","providerId",)

class ProvideHistoryAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=providerHistory
        fields =('date',"providerId","showroom_id","model","mark")
