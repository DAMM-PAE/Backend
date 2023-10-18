from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Cliente,FacturaMensual
import pandas as pd
from datetime import datetime
import json
# Create your views here.

def helloworld(request):
    return HttpResponse("Hello world!")

def inicializarBaseDatos(request):
    df = pd.read_excel("static/data/litros_board_22_23.xlsx")  # Reemplaza con la ubicación de tu archivo Excel
    df = df.fillna(0)
    df['fecha'].unique().tolist()
    df['fecha'] = df['fecha'].replace('ene-22', datetime(2022, 1, 1))
    df['mes'] = df['fecha'].dt.month
    df['año'] = df['fecha'].dt.year

    for i in range(len(df)):
        cliente = None
        if not Cliente.objects.filter(id=df["cliente"][i]).exists():
            cliente = Cliente(id=df["cliente"][i], nombre=df["cliente_nom"][i])
            cliente.save()
        else:
            cliente = Cliente.objects.get(id=df["cliente"][i])
        
        factura = FacturaMensual(idCliente=cliente, fechaFactura=datetime(df['año'][i].item(),df['mes'][i].item(),1), litrosEntregado=df["litros"][i])
        factura.save()
    return HttpResponse("Base de datos inicializada")
    
def getClientes(request):
    nombres = Cliente.objects.values_list('nombre', flat=True)
    nombres = list(nombres)
    return HttpResponse(json.dumps(nombres), content_type='application/json')

def getFacturas(request, nombreCliente):
    cliente = Cliente.objects.get(nombre=nombreCliente)
    facturas = FacturaMensual.objects.filter(idCliente=cliente)
    facturas = serializers.serialize('json', facturas)   
    return HttpResponse(facturas, content_type='application/json')