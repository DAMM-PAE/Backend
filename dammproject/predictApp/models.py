from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50,null=True)
    tipoBar = models.CharField(max_length=50,null=True)
    codigoPostal = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.nombre


class Entregas(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaPedido = models.DateField()
    fechaEntrega = models.DateField()
    litrosEntregados = models.IntegerField()

class FacturaMensual(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Opciones para el campo fechaFactura en el formulario ["m-Y"]
    fechaFactura = models.DateField(["%m-%Y"])
    litrosEntregado = models.FloatField()

    def __str__(self) -> str:
        return self.idCliente.nombre + " " + str(self.fechaFactura)

# class Camion(models.Model):
#     idMatricula = models.CharField(max_length=10, primary_key=True)
#     capacidad = models.IntegerField()


