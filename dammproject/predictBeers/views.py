from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictBeers.models import Bar, Entregas, FacturaMensual, IOT, Prediccion
from predictBeers.serializers import BarSerializer, EntregasSerializer, FacturaMensualSerializer, IOTSerializer, PrediccionSerializer
from .dataInit.listUser import initList
from dammproject.dammproject import settings
class InitDataBase(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        initList(settings.BASE_DIR + "/static/data/llistat.xlsx")
        return Response(status=status.HTTP_200_OK)

class BarList(APIView):
    """
    List all bars, or create a new bar.
    """
    def get(self, request, format=None):
        bars = Bar.objects.all()
        serializer = BarSerializer(bars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BarDetail(APIView):
    """
    Retrieve, update or delete a bar instance.
    """
    def get_object(self, pk):
        try:
            return Bar.objects.get(pk=pk)
        except Bar.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bar = self.get_object(pk)
        serializer = BarSerializer(bar)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bar = self.get_object(pk)
        serializer = BarSerializer(bar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bar = self.get_object(pk)
        bar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)