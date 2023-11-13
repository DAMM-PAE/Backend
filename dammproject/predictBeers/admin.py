from django.contrib import admin

# Register your models here.
from .models import Bar, Entregas, FacturaMensual, IOT, Prediccion

admin.site.register(Bar)
admin.site.register(Entregas)
admin.site.register(FacturaMensual)
admin.site.register(IOT)
admin.site.register(Prediccion)
