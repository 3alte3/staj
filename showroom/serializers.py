from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = showroom
        fields = ('id',"name","content","balance","location","showroom_id")


class Charact_ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = charact_showroom
        fields = ('engine_type','max_speed','ammount_of_eng','model','mark','showroom_id',)


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = ('id','engine_type','max_speed','ammount_of_eng','model','mark','price','showroom_id','ammount_of_cars',)


class HistorySerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    buyer = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    showroom_id = serializers.IntegerField()

class UniqueBuyersSerializer(serializers.ModelSerializer):
    class Meta :
        model = unique_buyers
        fields = ("buyer_id","showroom_id","amount_of_purchase")