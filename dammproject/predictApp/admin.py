from django.contrib import admin
from .models import Cliente,FacturaMensual
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'tipoBar', 'codigoPostal')
    search_fields = ('id', 'nombre', 'direccion', 'tipoBar', 'codigoPostal')

class FacturaMensualAdmin(admin.ModelAdmin):
    list_display = ('idCliente', 'fechaFactura', 'litrosEntregado')
    search_fields = ('idCliente', 'fechaFactura', 'litrosEntregado')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(FacturaMensual)


