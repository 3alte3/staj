from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class BuyerAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=buyer
        fields = ('id','name','surname','email','phoneNumber','buyerId','balance',)


class BuyerHistoryAPIViewSerializer(serializers.Serializer):
    buyerId = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    price = serializers.IntegerField()
    showroom_id = serializers.IntegerField()