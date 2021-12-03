from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.users.models import *

class Inasistencia(BaseModel):
    idInasistencia = models.BigAutoField(primary_key = True)
    fechaReporte = models.DateTimeField(auto_now_add=True)
    descripcionInasistencia = models.TextField()
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Inasistencia'
        verbose_name_plural = 'Inasistencias'

class TipoNovedad(BaseModel):
    id = models.BigAutoField(primary_key = True)
    tipoNovedad=models.CharField(max_length=30,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.tipoNovedad

    class Meta:
        verbose_name = 'Tipo Novedad'
        verbose_name_plural = 'Tipos de Novedad'

class Novedad (models.Model):
    fichaAspirante = models.IntegerField (blank=True,default=0)
    estadoNovedad = models.CharField(max_length=40)
    comentario = models.CharField(max_length=100,blank=True)
    fechaInicio = models.CharField(max_length=100,blank=True)
    causa = models.CharField(max_length=100,blank=True)
    duracionA = models.IntegerField (blank=True,default=0)
    acta = models.FileField(upload_to='solicitudes/',blank=True)
    fechaSolicitud= models.CharField(max_length=100)
    aprendizNovedad = models.ForeignKey(Aprendiz, on_delete = models.CASCADE)
    tipoNovedad = models.ForeignKey(TipoNovedad, on_delete = models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.aprendizNovedad)

    class Meta:
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'
  

class DetalleNovedad(Novedad):
    DescripcionNovedad = models.TextField(blank=True)


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.DescripcionNovedad)

    class Meta:
        verbose_name = 'Detalle de novedad'
        verbose_name_plural = 'Detalles de novedades'

