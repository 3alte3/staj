from rest_framework import serializers
from django_countries.serializer_fields import CountryField

class ShowroomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    balance = serializers.IntegerField()
    location = CountryField()
    showroom_id = serializers.IntegerField()
    isActive = serializers.BooleanField(default=True)

class Charact_ShowroomSerializer(serializers.Serializer):
    engine_type = serializers.CharField(max_length=255)
    max_speed = serializers.CharField(max_length=255)
    ammount_of_eng = serializers.IntegerField()
    model = serializers.CharField(max_length=255)
    mark = serializers.CharField(max_length=255)
    showroom_id = serializers.IntegerField()

class CarsSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=255)
    mark = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    showroom_id = serializers.IntegerField()

class HistorySerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    buyer = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    showroom_id = serializers.IntegerField()

class UniqueBuyersSerializer(serializers.Serializer):
    buyer_id = serializers.IntegerField()
    showroom_id = serializers.IntegerField()
