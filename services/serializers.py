from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class createOfferViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('buyer','maxPrice','mark','model',)

class statisticsViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('name','desc','content','date')