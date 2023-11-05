from django.db import models


# Create your models here.
class Bar(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50,null=True)
    ciutat = models.CharField(max_length=50,null=True)
    codiPostal = models.CharField(max_length=50,null=True)
    direccio = models.CharField(max_length=50,null=True)
    numCarrer = models.CharField(max_length=50,null=True)
    tipudBar = models.CharField(max_length=50,null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    def __str__(self) -> str:
        return self.nom
class Entregas(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fechaPedido = models.DateField()
    fechaEntrega = models.DateField()
    litrosEntregados = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nom + " " + str(self.fechaPedido)

class FacturaMensual(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fechaFactura = models.DateField()
    litrosEntregado = models.FloatField()

    def __str__(self) -> str:
        return self.idCliente.nom + " " + str(self.fechaFactura)

class IOT(models.Model):
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fecha = models.DateField()
    litros = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nom + " " + str(self.fecha)
    
class Prediccion(models.Model):
    id = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Bar, on_delete=models.CASCADE)
    fecha = models.DateField()
    litros = models.IntegerField()
    def __str__(self) -> str:
        return self.idCliente.nom + " " + str(self.fecha)