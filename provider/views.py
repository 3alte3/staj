from datetime import timezone

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from django.shortcuts import render

class ProviderAPIView(APIView):
    def get(self, request):
        lst = provider.objects.all()
        return Response({'posts': ProviderAPIViewSerializer(lst, many=True).data})

    def post(self, request):
        post_new = provider.objects.create(
            name=request.data['name'],
            date=timezone.now(),
            ammountOfBuyers=request.data['ammountOfBuyers'],
            providerId = request.data['providerId'],
        )
        return Response({'post': ProviderAPIViewSerializer(post_new).data})

    def delete(self,request):
        postToDel = provider.objects.get(name = request.data['name'],providerId = request.data['providerId'])
        postToDel.delete()
        return Response({'deleted' : ProviderAPIViewSerializer(postToDel).data})


class ListOfCarsAPIView(generics.ListCreateAPIView):
    queryset = listOfCars.objects.all()
    serializer_class=ListOfCarsAPIViewSerializer

class ListOfCarsAPIViewDelete(generics.DestroyAPIView):
    queryset = listOfCars.objects.all()
    serializer_class = ListOfCarsAPIViewSerializer

