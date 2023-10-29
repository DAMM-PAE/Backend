from django.db import models


# Create your models here.
class Bar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50,null=True)
    ciudad = models.CharField(max_length=50,null=True)
    codigoPostal = models.IntegerField(null=True)
    direccion = models.CharField(max_length=50,null=True)
    numeroCalle = models.CharField(max_length=50,null=True)
    tipoBar = models.CharField(max_length=50,null=True)
    
    def __str__(self) -> str:
        return self.nombre

class Entregas(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fechaPedido = models.DateField()
    fechaEntrega = models.DateField()
    litrosEntregados = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nombre + " " + str(self.fechaPedido)

class FacturaMensual(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fechaFactura = models.DateField()
    litrosEntregado = models.FloatField()

    def __str__(self) -> str:
        return self.idCliente.nombre + " " + str(self.fechaFactura)

class IOT(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fecha = models.DateField()
    litros = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nombre + " " + str(self.fecha)
    
class Prediccion(models.Model):
    id = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fecha = models.DateField()
    litros = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nombre + " " + str(self.fecha)