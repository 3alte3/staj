from datetime import timezone

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from django.shortcuts import render

class ProviderAPIView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ListOfCarsAPIViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['providerId', 'name']
    permission_classes = (IsAuthenticated,)


class ListOfCarsViewSet(viewsets.ModelViewSet):
    queryset = ListOfCars.objects.all()
    serializer_class=ListOfCarsAPIViewSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['price']
    search_fields = ['model', 'mark']
    permission_classes = (IsAuthenticated,)

class ProviderHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProviderHistory.objects.all()
    serializer_class = ProvideHistoryAPIViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model']
    search_fields = ['model', 'mark']
    permission_classes = (IsAuthenticated,)



