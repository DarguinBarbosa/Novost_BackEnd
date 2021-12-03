from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.novedades.models import *

class UpdateDetalle(serializers.ModelSerializer):
    class Meta:
        model = DetalleNovedad
        fields = ('DescripcionNovedad',)

class insertarNove(serializers.ModelSerializer):
    class Meta:
        model=DetalleNovedad
        fields=('__all__')

class DetalleNovedadSerializer(serializers.ModelSerializer):
    nombre=serializers.CharField(source = 'aprendizNovedad.nombresUsuario',read_only=True)
    apellido=serializers.CharField(source = 'aprendizNovedad.apellidosUsuario',read_only=True)
    correo=serializers.CharField(source = 'aprendizNovedad.email',read_only=True)
    t=serializers.CharField(source = 'tipoNovedad.tipoNovedad',read_only=True)
    ficha=serializers.CharField(source = 'aprendizNovedad.fichaAprendiz',read_only=True)
    class Meta:
        model=DetalleNovedad
        fields=('__all__')

class NovedadSerlizers(serializers.ModelSerializer):
    n=serializers.CharField(source = 'aprendizNovedad.numeroDocumentoUsuario',read_only=True)
    t=serializers.CharField(source = 'tipoNovedad.tipoNovedad',read_only=True)
    class Meta:
        model=Novedad
        fields=('id','acta','estadoNovedad','fechaSolicitud','aprendizNovedad','tipoNovedad','comentario','n','t')

class tipoNovedadSerlizers(serializers.ModelSerializer):
    class Meta:
        model=TipoNovedad
        fields=('id','tipoNovedad')

class solicitudUpdate(serializers.ModelSerializer):
    class Meta:
        model=Novedad
        fields=('estadoNovedad',)

class solicitudD(serializers.ModelSerializer):
    class Meta:
        model=Novedad
        fields=('estadoNovedad','comentario',)