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

class ProviderAPIView(APIView):
    queryset = provider.objects.all()
    serializer_class = ListOfCarsAPIViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['providerId', 'name']
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     lst = provider.objects.all()
    #     return Response({'posts': ProviderAPIViewSerializer(lst, many=True).data})
    #
    # def post(self, request):
    #     post_new = provider.objects.create(
    #         name=request.data['name'],
    #         date=timezone.now(),
    #         ammountOfBuyers=request.data['ammountOfBuyers'],
    #         providerId = request.data['providerId'],
    #     )
    #     return Response({'post': ProviderAPIViewSerializer(post_new).data})
    #
    # def delete(self,request):
    #     postToDel = provider.objects.get(name = request.data['name'],providerId = request.data['providerId'])
    #     postToDel.delete()
    #     return Response({'deleted' : ProviderAPIViewSerializer(postToDel).data})


class ListOfCarsViewSet(viewsets.ModelViewSet):
    queryset = listOfCars.objects.all()
    serializer_class=ListOfCarsAPIViewSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['price']
    search_fields = ['model', 'mark']
    permission_classes = (IsAuthenticated,)

class ProviderHistoryViewSet(viewsets.ModelViewSet):
    queryset = providerHistory.objects.all()
    serializer_class = ProvideHistoryAPIViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model']
    search_fields = ['model', 'mark']
    permission_classes = (IsAuthenticated,)



