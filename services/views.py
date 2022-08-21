from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class CreateOfferViewSet(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = createOfferViewSetSerializer
    permission_classes = (IsAuthenticated,)

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = statisticsViewSetSerializer
    permission_classes = (IsAuthenticated,)
