from django.urls import path
from apps.users.api.api import *

urlpatterns = [
    # USUARIO
    path('usuario/', user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>/', user_detail_view, name = 'usuario_detail_api_view'),
    # LISTA
    path('lista/', listas_api_view, name = 'listas'),
    # LISTA
    path('correo/<str:pk>/', correo_api_view, name = 'correos'),
    # APRENDIZ
    path('aprendiz/', aprendiz_api_view, name = 'aprendiz_api'),
    path('aprendiz/<int:pk>/', aprendiz_detail_view, name = 'aprendiz_detail_api_view'),
    path('aprendizF/<int:pk>/', fichaApe, name = 'Update_Ficha_Aprendiz'),
    # FICHA
    path('ficha/', ficha_api_view, name = 'ficha_api'),
    path('ficha/<int:pk>/', ficha_detail_view, name = 'ficha_detail_api_view'),
    # COORDINACION
    path('coordinacion/', coordinacion_api_view, name = 'coordinacion_api'),
    path('coordinacion/<int:pk>/', coordinacion_detail_view, name = 'coordinacion_detail_api_view'),
    # CENTRO
    path('centro/', centro_api_view, name = 'centro_api'),
    path('centro/<int:pk>/', centro_detail_view, name = 'centro_detail_api_view'),
    # COORDINADOR
    path('coordinador/', coordinador_api_view, name = 'coordinador_api'),
    path('coordinador/<int:pk>/', coordinador_detail_view, name = 'coordinador_detail_api_view'),
    # ASIGNATURA
    path('asignatura/', asignatura_api_view, name = 'asignatura_api'),
    path('asignatura/<int:pk>/', asignatura_detail_view, name = 'asignatura_detail_api_view'),
    # INSTRUCTOR
    path('instructor/', instructor_api_view, name = 'instructor_api'),
    path('instructor/<int:pk>/', instructor_detail_view, name = 'instructor_detail_api_view'),
    # APOYO ADMINISTRATIVO
    path('apoyoAdministrativo/', apoyo_administrativo_api_view, name = 'apoyo_administrativo_api'),
    path('apoyoAdministrativo/<int:pk>/', apoyo_administrativo_detail_view, name = 'apoyo_administrativo_detail_api_view'),
    # ADMINISTRADOR
    path('administrador/', administrador_api_view, name = 'administrador_api'),
    path('administrador/<int:pk>/', administrador_detail_view, name = 'administrador_detail_api_view'),
]