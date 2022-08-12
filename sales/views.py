from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from djsite.staj.sales.models import discount


class discountAPIView(viewsets.ModelViewSet):
    queryset = discount.objects.all()
    serializer_class = discountserializer
    permission_classes = (IsAuthenticated,)
