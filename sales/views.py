from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Discount


class DiscountAPIView(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['model', 'mark', 'provider_id']


class DiscountOfShowroomsAPI(viewsets.ModelViewSet):
    queryset = DiscountOfShowrooms.objects.all()
    serializer_class = DiscountOfShowroomsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['model', 'mark', 'showroom__name']
