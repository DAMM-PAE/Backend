from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Cliente,FacturaMensual
import pandas as pd
import datetime
# Create your views here.

def helloworld(request):
    return HttpResponse("Hello world!")

def inicializarBaseDatos(request):
    df = pd.read_excel("static/data/litros_board_22_23.xlsx")  # Reemplaza con la ubicación de tu archivo Excel
    df = df.fillna(0)
    df['fecha'].unique().tolist()
    df['fecha'] = df['fecha'].replace('ene-22', datetime.datetime(2022, 1, 1))


    for i in range(len(df)):
        cliente = None
        if not Cliente.objects.filter(id=df["cliente"][i]).exists():
            cliente = Cliente(id=df["cliente"][i], nombre=df["cliente_nom"][i])
            cliente.save()
        else:
            cliente = Cliente.objects.get(id=df["cliente"][i])
        factura = FacturaMensual(idCliente=cliente, fechaFactura=df["fecha"][i], litrosEntregado=df["litros"][i])
        factura.save()
    return HttpResponse("Base de datos inicializada")
    
