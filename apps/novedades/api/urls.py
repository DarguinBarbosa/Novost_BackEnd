from django.urls import path
from apps.novedades.api.api import *

urlpatterns=[
    path('denovedad/', detalleApi, name = 'Detalles de novedades'),
    path('denovedad/<int:pk>/', getId, name = 'Detalle de novedad'),
    path('novedad/', NovedadApi, name = 'Novedades'),
    path('crearnovedad/', insertar, name = 'Crear novedad'),
    path('novedad/<int:pk>/', NovedadApi, name = 'Novedad'),
    path('novedades/<int:pk>/', getnove, name = 'Novedades'),
    path('aprendiz/<int:pk>/', AprendizNovedad, name = 'Aprendiz Novedad'),
    path('tipo/novedad', tipoNovedadApi, name = 'Tipo de novedad'),
    path('tipo/novedad/<int:pk>/', tipoNovedadApi, name = 'Tipo de novedad'),
    path('tipo/novedades/<int:pk>/', getId1, name = 'Tipos de novedad'),
    path('solicitudA', UpdateEstadoNo, name = 'Solicitud'),
    path('denegar', solicitud, name = 'Denegar'),
    path('tip', post, name = 'Tip')
]