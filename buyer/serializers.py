from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class BuyerAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyer
        fields = ('id','name','surname','email','phoneNumber','balance',)


class BuyerHistoryAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerHistory
        fields = ('id','buyer','date','price','showroom')
