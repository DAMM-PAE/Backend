from .models import Bar, Entregas, FacturaMensual, Prediccion
from rest_framework import serializers

class BarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nom = serializers.CharField(required=True)
    provincia = serializers.CharField(required=False)
    ciutat = serializers.CharField(required=False)
    codiPostal = serializers.IntegerField(required=False)
    direccio = serializers.CharField(required=False)
    numCarrer = serializers.CharField(required=False)
    tipusBar = serializers.CharField(required=False)
    latitud = serializers.FloatField(required=False)
    longitud = serializers.FloatField(required=False)
    data = serializers.DateField(required=False)

    iot = serializers.BooleanField(required=False)
    percentatge = serializers.FloatField(required=False)
    def create(self, validated_data):
        # Create new Bar with unique nombre
        name = validated_data.get('nom')
        if Bar.objects.filter(nom=name).exists():
            raise serializers.ValidationError("Bar with name " + name + " already exists")
        return Bar.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        instance.provincia = validated_data.get('provincia', instance.provincia)
        instance.ciutat = validated_data.get('ciutat', instance.ciutat)
        instance.codiPostal = validated_data.get('codiPostal', instance.codiPostal)
        instance.direccio = validated_data.get('direccio', instance.direccio)
        instance.numCarrer = validated_data.get('numCarrer', instance.numCarrer)
        instance.latitud = validated_data.get('latitud', instance.latitud)
        instance.longitud = validated_data.get('longitud', instance.longitud)
        instance.tipusBar = validated_data.get('tipusBar', instance.tipusBar)
        instance.data = validated_data.get('data', instance.data)
        instance.iot = validated_data.get('iot', instance.iot)
        instance.percentatge = validated_data.get('percentatge', instance.percentatge)
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

# class IOTSerializer(serializers.ModelSerializer):
#     idCliente = serializers.PrimaryKeyRelatedField(queryset=Bar.objects.all())
#     fecha = serializers.DateField(required=True)
#     litros = serializers.IntegerField(required=True)
    
#     def create(self, validated_data):
#         return IOT.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.idCliente = validated_data.get('idCliente', instance.idCliente)
#         instance.fecha = validated_data.get('fecha', instance.fecha)
#         instance.litros = validated_data.get('litros', instance.litros)
#         instance.save()
#         return instance
    
#     class Meta:
#         model = IOT
#         fields = "__all__"

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

