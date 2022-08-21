from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerAPIViewSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['balance']
    permission_classes = (IsAuthenticated,)
    search_fields = ['name','surname','buyer__name']


class BuyerHistoryViewSet(viewsets.ModelViewSet):
    queryset = BuyerHistory.objects.all()
    serializer_class = BuyerHistoryAPIViewSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['price']
    permission_classes = (IsAuthenticated,)
    search_fields=['buyer__name','showroom__name1']



