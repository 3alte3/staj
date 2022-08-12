from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import *

class createOfferViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = offers
        fields = ('buyerId','maxPrice','mark','model',)