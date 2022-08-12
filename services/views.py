from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class createOfferViewSet(viewsets.ModelViewSet):
    queryset = offers.objects.all()
    serializer_class = createOfferViewSetSerializer
    permission_classes = (IsAuthenticated,)
