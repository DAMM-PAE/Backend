from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictBeers.models import Bar, Entregas, FacturaMensual, IOT, Prediccion
from predictBeers.serializers import BarSerializer, EntregasSerializer, FacturaMensualSerializer, IOTSerializer, PrediccionSerializer
import pandas as pd
import datetime

def initListaC():
        df = pd.read_excel('static/data/llistat.xlsx')

        for _, row in df.iterrows():
            if Bar.objects.filter(nom=row['nombre']).exists():
                continue
            bar = Bar.objects.create(nom=row['nombre'],ciutat=row['ciudad'],direccio=row['direccion'],numCarrer=row['numeroCalle'],tipudBar=row['tipoBar'])
            bar.save()

def iniListaBoard():
        df = pd.read_excel('static/data/litros_board_22_23.xlsx')
        df = df.fillna(0)
        #df['fecha'] = df['fecha'].replace('ene-22', datetime.datetime(2022, 1, 1))

        for _, row in df.iterrows():
            try:
                bar = Bar.objects.filter(nom=row['cliente_nom'])
                
                if not bar.exists():
                    bar = Bar.objects.create(nom = row['cliente_nom'])
                    bar.save()
                else:
                    bar = bar[0]
                año = row['fecha'].year
                mes = row['fecha'].month
                dia = row['fecha'].day
                fecha = datetime.datetime(año,mes,dia)
                if FacturaMensual.objects.filter(idCliente=bar,fechaFactura=fecha).exists():
                    continue

                factura = FacturaMensual.objects.create(idCliente=bar,fechaFactura=fecha,litrosEntregado=row['litros'])
                factura.save()
            except:
                print("Error en la fila: ", row)
                continue
    
            

class InitData(APIView):
    def get(self,request):
        initListaC()
        iniListaBoard()
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


class EntregasList(APIView):
    """
    List all entregas, or create a new entrega.
    """
    def get(self, request, format=None):
        entregas = Entregas.objects.all()
        serializer = EntregasSerializer(entregas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntregasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EntregasDetail(APIView):

    """
    Retrieve, update or delete a entrega instance.
    """
    def get_object(self, pk):
        try:
            return Entregas.objects.get(pk=pk)
        except Entregas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entrega = self.get_object(pk)
        serializer = EntregasSerializer(entrega)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entrega = self.get_object(pk)
        serializer = EntregasSerializer(entrega, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entrega = self.get_object(pk)
        entrega.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FacturaMensualList(APIView):

    """
    List all facturas mensuales, or create a new factura mensual.
    """
    def get(self, request, format=None):
        facturasMensuales = FacturaMensual.objects.all()
        serializer = FacturaMensualSerializer(facturasMensuales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacturaMensualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FacturaMensualDetail(APIView):

    """
    Retrieve, update or delete a factura mensual instance.
    """
    def get_object(self, pk):
        try:
            return FacturaMensual.objects.get(pk=pk)
        except FacturaMensual.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        facturaMensual = self.get_object(pk)
        serializer = FacturaMensualSerializer(facturaMensual)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        facturaMensual = self.get_object(pk)
        serializer = FacturaMensualSerializer(facturaMensual, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        facturaMensual = self.get_object(pk)
        facturaMensual.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class IOTList(APIView):

    """
    List all IOTs, or create a new IOT.
    """
    def get(self, request, format=None):
        iots = IOT.objects.all()
        serializer = IOTSerializer(iots, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IOTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IOTDetail(APIView):

    """
    Retrieve, update or delete a IOT instance.
    """
    def get_object(self, pk):
        try:
            return IOT.objects.get(pk=pk)
        except IOT.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        iot = self.get_object(pk)
        serializer = IOTSerializer(iot)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        iot = self.get_object(pk)
        serializer = IOTSerializer(iot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        iot = self.get_object(pk)
        iot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PrediccionList(APIView):
    
        """
        List all Predicciones, or create a new Prediccion.
        """
        def get(self, request, format=None):
            predicciones = Prediccion.objects.all()
            serializer = PrediccionSerializer(predicciones, many=True)
            return Response(serializer.data)
    
        def post(self, request, format=None):
            serializer = PrediccionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

