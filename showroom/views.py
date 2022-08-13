import datetime
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = showroom.objects.all()
    serializer_class = ShowroomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['showroom_id']
    search_fields = ('showroom_id','name')

class CharactViewSet(viewsets.ModelViewSet):
    queryset = charact_showroom.objects.all()
    serializer_class = Charact_ShowroomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model','mark']
    search_fields = ('model','mark')

class CarsViewSet(viewsets.ModelViewSet):
    queryset = cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model', 'mark','price']
    search_fields = ('model', 'mark','showroom_id')

class HistoryAPIView(APIView):
    def get(self, request):
        lst = history.objects.all()
        return Response({'posts': HistorySerializer(lst, many=True).data})

    def post(self, request):
        post_new = history.objects.create(
            date=timezone.now(),
            buyer=request.data['buyer'],
            price=request.data['price'],
            showroom_id=request.data['showroom_id'],
        )
        return Response({'post': HistorySerializer(post_new).data})


class UniqueBuyersAPIView(viewsets.ModelViewSet):
    queryset = unique_buyers.objects.all()
    serializer_class = UniqueBuyersSerializer





