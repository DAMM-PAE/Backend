from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictBeers.models import Bar, Entregas, FacturaMensual, IOT, Prediccion
from predictBeers.serializers import BarSerializer, EntregasSerializer, FacturaMensualSerializer, IOTSerializer, PrediccionSerializer
from .dataInit.listUser import initList
from dammproject import settings
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

import pandas as pd 
from .serializers import UploadSerializer
from rest_framework.viewsets import ViewSet
class UploadExcel(ViewSet):
    """
    Upload and process an Excel file to update the list of bars.
    """
    serializer_class = UploadSerializer
    def list(self, request):
        return Response(status=status.HTTP_200_OK, data={"message": "Upload an Excel file to update the list of bars."})
    
    def create(self, request):
        file = request.FILES.get('file') 
        
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.xls') and not file.name.endswith('.xlsx'):
            return Response({"error": "Invalid file format. Only Excel files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_excel(file)
            # Assuming your Excel file has columns 'name', 'location', etc. matching your Bar model
            # You can update the bars based on the data in the Excel file.
            for index, row in df.iterrows():
                bar_data = {
                    'nombre': row['nombre'],
                    'direccion': row['direccion'],
                    'numeroCalle': row['numeroCalle'],
                    'tipoBar': row['tipoBar'],
                    'ciudad': row['ciudad'],
                    'provincia': row['provincia'],
                    # Add other columns as needed
                }
                serializer = BarSerializer(data=bar_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f"Error processing row {index}: {serializer.errors}")
            return Response({"message": "Excel file processed successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
