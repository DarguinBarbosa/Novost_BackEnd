from django.db import models

class BaseModel(models.Model):
    state = models.BooleanField('Estado', default=True)
    fecha_creacion =  models.DateField('Fecha creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion =  models.DateField('Fecha modificacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion =  models.DateField('Fecha eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
