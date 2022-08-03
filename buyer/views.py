from django.utils import timezone
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *



class BuyerAPIView(generics.ListCreateAPIView):
    queryset = buyer.objects.all()
    serializer_class = BuyerAPIViewSerializer

class BuyerAPIViewDelete(generics.DestroyAPIView):
    queryset = buyer.objects.all()
    serializer_class = BuyerAPIViewSerializer



class BuyerHistoryAPIView(APIView):
    def get(self, request):
        lst = buyer_history.objects.all()
        return Response({'posts': BuyerHistoryAPIViewSerializer(lst, many=True).data})

    def post(self, request):
        post_new = buyer_history.objects.create(
            buyerId=request.data['buyerId'],
            date=timezone.now(),
            price=request.data['price'],
            showroom_id = request.data['showroom_id'],
        )
        return Response({'post': BuyerHistoryAPIViewSerializer(post_new).data})

    def delete(self,request):
        postToDel = buyer_history.objects.get(buyerId = request.data['buyerId'])
        postToDel.delete()
        return Response({'deleted' : BuyerHistoryAPIViewSerializer(postToDel).data})