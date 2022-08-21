from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class ProviderAPIViewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Provider
        fields = ("name","date","ammountOfBuyers","provider",)


class ListOfCarsAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListOfCars
        fields =('id',"engine_type","max_speed","ammount_of_eng","model","mark","price","provider",)

class ProvideHistoryAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProviderHistory
        fields =('date',"provider","showroom","model","mark")
