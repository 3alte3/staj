import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ShowroomAPIView(APIView):
    def get(self, request):
        lst = showroom.objects.all()
        return Response({'posts': ShowroomSerializer(lst, many=True).data})

    def post(self, request):
        post_new = showroom.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            balance=request.data['balance'],
            location = request.data['location'],
            showroom_id=request.data['showroom_id']
        )
        return Response({'post': ShowroomSerializer(post_new).data})

    def delete(self,request):
        postToDel = showroom.objects.get(showroom_id = request.data['showroom_id'])
        postToDel.delete()
        return Response({'deleted' : ShowroomSerializer(postToDel).data})

class Charact_ShowroomAPIView(APIView):
    def get(self, request):
        lst = charact_showroom.objects.all()
        return Response({'posts': Charact_ShowroomSerializer(lst, many=True).data})

    def post(self, request):
        post_new = charact_showroom.objects.create(
            engine_type=request.data['engine_type'],
            max_speed=request.data['max_speed'],
            ammount_of_eng=request.data['ammount_of_eng'],
            model = request.data['model'],
            mark=request.data['mark'],
            showroom_id = request.data['showroom_id']
        )
        return Response({'post': Charact_ShowroomSerializer(post_new).data})

    def delete(self,request):
        postToDel = charact_showroom.objects.get(model = request.data['model'],mark = request.data['mark'])
        postToDel.delete()
        return Response({'deleted' : Charact_ShowroomSerializer(postToDel).data})

class CarsAPIView(APIView):
    def get(self, request):
        lst = cars.objects.all()
        return Response({'posts': CarsSerializer(lst, many=True).data})

    def post(self, request):
        post_new = cars.objects.create(
            model=request.data['model'],
            mark=request.data['mark'],
            price=request.data['price'],
            showroom_id = request.data['showroom_id'],
        )
        return Response({'post': CarsSerializer(post_new).data})

    def delete(self,request):
        postToDel = cars.objects.get(model = request.data['model'],mark = request.data['mark'])
        postToDel.delete()
        return Response({'deleted' : CarsSerializer(postToDel).data})

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


class UniqueBuyersAPIView(APIView):
    def get(self, request):
        lst = unique_buyers.objects.all()
        return Response({'posts': UniqueBuyersSerializer(lst, many=True).data})

    def post(self, request):
        post_new = unique_buyers.objects.create(
            buyer_id=request.data['buyer_id'],
            showroom_id=request.data['showroom_id'],
        )
        return Response({'post': UniqueBuyersSerializer(post_new).data})



