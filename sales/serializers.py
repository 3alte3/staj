from rest_framework import serializers
from .models import *


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ("start","end","model","mark",
                  "provider","description","name","percent",)

class DiscountOfShowroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ("start","end","model","mark",
                  "showroom","description","name","percent",)