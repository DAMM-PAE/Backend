from .models import Bar, Entregas, FacturaMensual, IOT, Prediccion
from rest_framework import serializers

class BarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(required=True)
    provincia = serializers.CharField(required=False)
    ciudad = serializers.CharField(required=False)
    codigoPostal = serializers.IntegerField(required=False)
    direccion = serializers.CharField(required=False)
    numeroCalle = serializers.CharField(required=False)
    tipoBar = serializers.CharField(required=False)

    def create(self, validated_data):
        return Bar.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.provincia = validated_data.get('provincia', instance.provincia)
        instance.ciudad = validated_data.get('ciudad', instance.ciudad)
        instance.codigoPostal = validated_data.get('codigoPostal', instance.codigoPostal)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.numeroCalle = validated_data.get('numeroCalle', instance.numeroCalle)
        instance.tipoBar = validated_data.get('tipoBar', instance.tipoBar)
        instance.save()
        return instance

    class Meta:
        model = Bar
        fields = "__all__"

class EntregasSerializer(serializers.ModelSerializer):
    idCliente = serializers.PrimaryKeyRelatedField(queryset=Bar.objects.all())
    fechaPedido = serializers.DateField(required=True)
    fechaEntrega = serializers.DateField(required=True)
    litrosEntregados = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Entregas.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.idCliente = validated_data.get('idCliente', instance.idCliente)
        instance.fechaPedido = validated_data.get('fechaPedido', instance.fechaPedido)
        instance.fechaEntrega = validated_data.get('fechaEntrega', instance.fechaEntrega)
        instance.litrosEntregados = validated_data.get('litrosEntregados', instance.litrosEntregados)
        instance.save()
        return instance
    
    class Meta:
        model = Entregas
        fields = "__all__"

class FacturaMensualSerializer(serializers.ModelSerializer):
    idCliente = serializers.PrimaryKeyRelatedField(queryset=Bar.objects.all())
    fechaFactura = serializers.DateField(required=True)
    litrosEntregado = serializers.FloatField(required=True)
    
    def create(self, validated_data):
        return FacturaMensual.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.idCliente = validated_data.get('idCliente', instance.idCliente)
        instance.fechaFactura = validated_data.get('fechaFactura', instance.fechaFactura)
        instance.litrosEntregado = validated_data.get('litrosEntregado', instance.litrosEntregado)
        instance.save()
        return instance

    class Meta:
        model = FacturaMensual
        fields = "__all__"

class IOTSerializer(serializers.ModelSerializer):
    idCliente = serializers.PrimaryKeyRelatedField(queryset=Bar.objects.all())
    fecha = serializers.DateField(required=True)
    litros = serializers.IntegerField(required=True)
    
    def create(self, validated_data):
        return IOT.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.idCliente = validated_data.get('idCliente', instance.idCliente)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.litros = validated_data.get('litros', instance.litros)
        instance.save()
        return instance
    
    class Meta:
        model = IOT
        fields = "__all__"

class PrediccionSerializer(serializers.ModelSerializer):
    
    idCliente = serializers.PrimaryKeyRelatedField(queryset=Bar.objects.all())
    fecha = serializers.DateField(required=True)
    litros = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Prediccion.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.idCliente = validated_data.get('idCliente', instance.idCliente)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.litros = validated_data.get('litros', instance.litros)
        instance.save()
        return instance
    
    class Meta:
        model = Prediccion
        fields = "__all__"

