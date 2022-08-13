from rest_framework import serializers
from .models import *


class discountserializer(serializers.ModelSerializer):
    class Meta:
        model = discount
        fields = ("start","end","model","mark",
                  "showroom_id","description","name","percent",)