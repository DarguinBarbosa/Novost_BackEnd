from django.conf import settings
from pandas.core.frame import DataFrame
from rest_framework.exceptions import bad_request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.api.serializers import *
from apps.users.models import *
from rest_framework import status
import pandas as pd
from apps.users.resources import AprendizResource
from tablib import Dataset
from django.core.mail import send_mail, EmailMessage
from django.template import loader
import os
from pathlib import Path
import random

permission_classes = [IsAuthenticated]

##################################################################################################################################
#### USUARIO ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        user_serializer = UserSerializer(data = request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def user_detail_view(request, pk):
    user = User.objects.filter(id = pk).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un usuario con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### CORREOS ####
##################################################################################################################################

@api_view(['POST'])
def correo_api_view(request, pk):
    print(pk)
    if request.method == "POST": 
        try:
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            NUMBER = "0123456789"
            symbol = "-_$*#@%&"
            all = lower + upper + NUMBER + symbol
            length = 12
            password = "".join(random.sample(all, length))
            email_from = settings.EMAIL_HOST_USER
            aprendiz = Aprendiz.objects.filter(email = pk).first()
            recipent_list = [aprendiz.email]
            html_message = loader.render_to_string(
                "correo.html",
                {
                    'user_name': aprendiz.nombresUsuario,
                    'documento': aprendiz.numeroDocumentoUsuario,
                    'contra': password,
                    'subject':  "Gracias",
                })
            send_mail("Grupo Novost", "", email_from, recipent_list,fail_silently=True,html_message=html_message)
            
            apr = {
                'id':aprendiz.id,
                'nombresUsuario':aprendiz.nombresUsuario,
                'email' :aprendiz.email,
                'password' :password,
            }

            aprendiz_serializer = AprendizContraCorreoSerializer(aprendiz, data = apr)

            if aprendiz_serializer.is_valid():
                aprendiz_serializer.save()           
                return Response({'message': 'El correo ha sido enviado con exito', 'nombre':aprendiz.nombresUsuario}, status=status.HTTP_200_OK)  
        except AttributeError:
            return Response({'message': 'El correo no fue enviado porque el correo no existe en la base de datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### APRENDIZ ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def aprendiz_api_view(request):
    if request.method == 'GET':
        aprendices = Aprendiz.objects.all()
        aprendices_serializer = AprendizSerializer(aprendices, many = True)
        return Response(aprendices_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        aprendiz_serializer = AprendizSerializer(data = request.data)
        
        if aprendiz_serializer.is_valid():
            aprendiz_serializer.save()
            return Response(aprendiz_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(aprendiz_serializer.errors)


@api_view(['PUT'])
def fichaApe (request,pk):
    aprendiz = Aprendiz.objects.filter(id = pk).first()
    if request.method == 'PUT':
        aprendiz_serializer = updateFichaApe(aprendiz, data = request.data)
        if aprendiz_serializer.is_valid(True):
                aprendiz_serializer.save()
                return Response(aprendiz_serializer.data)
        return Response(aprendiz_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def aprendiz_detail_view(request, pk):
    aprendiz = Aprendiz.objects.filter(id = pk).first()
    if aprendiz:
        if request.method == 'GET':
            aprendiz_serializer = AprendizSerializer(aprendiz)
            return Response(aprendiz_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            aprendiz_serializer = AprendizSerializer(aprendiz, data = request.data)
            if aprendiz_serializer.is_valid():
                aprendiz_serializer.save()
                return Response(aprendiz_serializer.data)
            return Response(aprendiz_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            aprendiz.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un aprendiz con tales datos'}, status=status.HTTP_400_BAD_REQUEST)

##################################################################################################################################
#### FICHA ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def ficha_api_view(request):
    if request.method == 'GET':
        fichas = Ficha.objects.all()
        fichas_serializer = FichaSerializer(fichas, many = True)
        return Response(fichas_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ficha_serializer = FichaSerializer(data = request.data)

        if ficha_serializer.is_valid():
            ficha_serializer.save()
            return Response(ficha_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(ficha_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def ficha_detail_view(request, pk):
    ficha = Ficha.objects.filter(idFicha = pk).first()
    if ficha:
        if request.method == 'GET':
            ficha_serializer = FichaSerializer(ficha)
            return Response(ficha_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            ficha_serializer = FichaSerializer(ficha, data = request.data)
            if ficha_serializer.is_valid():
                ficha_serializer.save()
                return Response(ficha_serializer.data)
            return Response(ficha_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            ficha.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay una ficha con tales datos'}, status=status.HTTP_400_BAD_REQUEST)
    
##################################################################################################################################
#### COORDINACION ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def coordinacion_api_view(request):
    if request.method == 'GET':
        coordinaciones = Coordinacion.objects.all()
        coordinaciones_serializer = CoordinacionSerializer(coordinaciones, many = True)
        return Response(coordinaciones_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        coordinacion_serializer = CoordinacionSerializer(data = request.data)
        
        if coordinacion_serializer.is_valid():
            coordinacion_serializer.save()
            return Response(coordinacion_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(coordinacion_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def coordinacion_detail_view(request, pk):
    coordinacion = Coordinacion.objects.filter(idCoordinacion = pk).first()
    if coordinacion:
        if request.method == 'GET':
            coordinacion_serializer = CoordinacionSerializer(coordinacion)
            return Response(coordinacion_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            coordinacion_serializer = CoordinacionSerializer(coordinacion, data = request.data)
            if coordinacion_serializer.is_valid():
                coordinacion_serializer.save()
                return Response(coordinacion_serializer.data)
            return Response(coordinacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            coordinacion.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay una coordinacion con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### CENTRO ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def centro_api_view(request):
    if request.method == 'GET':
        centros = Centro.objects.all()
        centros_serializer = CentroSerializer(centros, many = True)
        return Response(centros_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        centro_serializer = CentroSerializer(data = request.data)
        
        if centro_serializer.is_valid():
            centro_serializer.save()
            return Response(centro_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(centro_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def centro_detail_view(request, pk):
    centro = Centro.objects.filter(idCentro = pk).first()
    if centro:
        if request.method == 'GET':
            centro_serializer = CentroSerializer(centro)
            return Response(centro_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            centro_serializer = CentroSerializer(centro, data = request.data)
            if centro_serializer.is_valid():
                centro_serializer.save()
                return Response(centro_serializer.data)
            return Response(centro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            centro.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un centro con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### COORDINADOR ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def coordinador_api_view(request):
    if request.method == 'GET':
        coordinadores = Coordinador.objects.all()
        coordinadores_serializer = CoordinadorSerializer(coordinadores, many = True)
        return Response(coordinadores_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        coordinador_serializer = CoordinadorSerializer(data = request.data)
  
        if coordinador_serializer.is_valid():
            coordinador_serializer.save()
            return Response(coordinador_serializer.data, status=status.HTTP_201_CREATED)
        return Response(coordinador_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def coordinador_detail_view(request, pk):
    coordinador = Coordinador.objects.filter(id = pk).first()
    if coordinador:
        if request.method == 'GET':
            coordinador_serializer = CoordinadorSerializer(coordinador)
            return Response(coordinador_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            coordinador_serializer = CoordinadorSerializer(coordinador, data = request.data)  
            if coordinador_serializer.is_valid():
                coordinador_serializer.save()
                return Response(coordinador_serializer.data)
            return Response(coordinador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            coordinador.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un coordinador con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### ASIGNATURA ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def asignatura_api_view(request):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        asignaturas_serializer = AsignaturaSerializer(asignaturas, many = True)
        return Response(asignaturas_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        asignatura_serializer = AsignaturaSerializer(data = request.data)
        
        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return Response(asignatura_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(asignatura_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def asignatura_detail_view(request, pk):
    asignatura = Asignatura.objects.filter(idAsignatura = pk).first()
    if asignatura:
        if request.method == 'GET':
            asignatura_serializer = AsignaturaSerializer(asignatura)
            return Response(asignatura_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            asignatura_serializer = AsignaturaSerializer(asignatura, data = request.data)
            if asignatura_serializer.is_valid():
                asignatura_serializer.save()
                return Response(asignatura_serializer.data)
            return Response(asignatura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            asignatura.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay una asignatura con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### INSTRUCTOR ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def instructor_api_view(request):
    if request.method == 'GET':
        instructores = Instructor.objects.all()
        instructores_serializer = InstructorSerializer(instructores, many = True)
        return Response(instructores_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        instructor_serializer = InstructorSerializer(data = request.data)
        
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return Response(instructor_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(instructor_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def instructor_detail_view(request, pk):
    instructor = Instructor.objects.filter(id = pk).first()
    if instructor:
        if request.method == 'GET':
            instructor_serializer = InstructorSerializer(instructor)
            return Response(instructor_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            instructor_serializer = InstructorSerializer(instructor, data = request.data)
            if instructor_serializer.is_valid():
                instructor_serializer.save()
                return Response(instructor_serializer.data)
            return Response(instructor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            instructor.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un instructor con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### APOYO ADMINISTRATIVO ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def apoyo_administrativo_api_view(request):
    if request.method == 'GET':
        apoyos_administrativos = ApoyoAdministrativo.objects.all()
        apoyos_administrativos_serializer = ApoyoAdministrativoSerializer(apoyos_administrativos, many = True)
        return Response(apoyos_administrativos_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        apoyo_administrativo_serializer = ApoyoAdministrativoSerializer(data = request.data)
        
        if apoyo_administrativo_serializer.is_valid():
            apoyo_administrativo_serializer.save()
            return Response(apoyo_administrativo_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(apoyo_administrativo_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def apoyo_administrativo_detail_view(request, pk):
    apoyo_administrativo = ApoyoAdministrativo.objects.filter(id = pk).first()
    if apoyo_administrativo:
        if request.method == 'GET':
            apoyo_administrativo_serializer = ApoyoAdministrativoSerializer(apoyo_administrativo)
            return Response(apoyo_administrativo_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            apoyo_administrativo_serializer = ApoyoAdministrativoSerializer(apoyo_administrativo, data = request.data)
            if apoyo_administrativo_serializer.is_valid():
                apoyo_administrativo_serializer.save()
                return Response(apoyo_administrativo_serializer.data)
            return Response(apoyo_administrativo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            apoyo_administrativo.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un apoyo administrativo con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### ADMINISTRADOR ####
##################################################################################################################################

@api_view(['GET', 'POST'])
def administrador_api_view(request):
    if request.method == 'GET':
        administradores = Administrador.objects.all()
        administradores_serializer = AdministradorSerializer(administradores, many = True)
        return Response(administradores_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data['password'] = request.data['numeroDocumentoUsuario']
        administrador_serializer = AdministradorSerializer(data = request.data)
        
        if administrador_serializer.is_valid():
            administrador_serializer.save()
            return Response(administrador_serializer.data,  status=status.HTTP_201_CREATED)
        return Response(administrador_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def administrador_detail_view(request, pk):
    administrador = Administrador.objects.filter(id = pk).first()
    if administrador:
        if request.method == 'GET':
            administrador_serializer = AdministradorSerializer(administrador)
            return Response(administrador_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            administrador_serializer = AdministradorSerializer(administrador, data = request.data)
            if administrador_serializer.is_valid():
                administrador_serializer.save()
                return Response(administrador_serializer.data)
            return Response(administrador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            administrador.delete()
            return Response({'message': 'Eliminado con exito'}, status=status.HTTP_200_OK)
    return Response({'message': 'No hay un administrador con tales datos'}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################################################
#### LISTAS ####
##################################################################################################################################

@api_view(['POST','GET'])
def listas_api_view(request):
    if request.method == 'GET':
        aprendices = Aprendiz.objects.all()
        aprendices_serializer = AprendizSerializer(aprendices, many = True)
        return Response(aprendices_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        nueva_lista_aprendices = request.FILES['file']
       ######################################
        ## SI ESTA CONTROLANDO DUPLICIDAD, HAY QUE METERLE LOS MENSAJES Y HACER UNA CONSULTA PARA RETORNAR CUAL ES EL DATO QUE 
        ## ESTA REPETIDO
        ######################################

        if not nueva_lista_aprendices.name.endswith(('.xls','.xlsx')):
            return Response("No se puede cargar un archivo diferente a la extension xls(x)")
        df = pd.read_excel(nueva_lista_aprendices, header=4).fillna(0)
        df = df.assign(fichaAprendiz = request.POST.get('fichaAprendiz'))
        df = df.assign(rolUsuario = request.POST.get('rolUsuario'))
        df = df.assign(password = df['Número de Documento']) 
        df = df.rename(
            columns={
            'Tipo de Documento': 'tipoDocumentoUsuario',
            'Número de Documento': 'numeroDocumentoUsuario',
            'Nombre': 'nombresUsuario',
            'Apellidos': 'apellidosUsuario',
            'Correo Electrónico': 'email',
            'Celular': 'telefonoAprendiz',
            'Estado': 'estadoAprendiz',
            }
        )
        df = df[
            [
                'tipoDocumentoUsuario',
                'numeroDocumentoUsuario',
                'nombresUsuario',
                'apellidosUsuario',
                'email',
                'telefonoAprendiz', 
                'estadoAprendiz',
                'fichaAprendiz',
                'password',
                'rolUsuario'
            ]
        ] 
        df = df.set_index('tipoDocumentoUsuario')
        df = df.to_excel(f"{settings.BASE_DIR}\\..\\apps\\users\\api\\docs\\doc.xlsx")
        dataset = Dataset()
        imported_data = dataset.load(pd.read_excel(f"{settings.BASE_DIR}\\..\\apps\\users\\api\\docs\\doc.xlsx"))
      
        for i in range(len(imported_data)):
            aprendiz = {
            'tipoDocumentoUsuario' :imported_data[i][0],
            'numeroDocumentoUsuario' :imported_data[i][1],
            'nombresUsuario' :imported_data[i][2],
            'apellidosUsuario' :imported_data[i][3],
            'email' :imported_data[i][4],
            'telefonoAprendiz' :imported_data[i][5],
            'estadoAprendiz' :imported_data[i][6],
            'fichaAprendiz' :imported_data[i][7],
            'password' :imported_data[i][8],
            'rolUsuario' :imported_data[i][9]
            }

            aprendiz_serializer = AprendizSerializer(data = aprendiz)
            if aprendiz_serializer.is_valid(True):
                aprendiz_serializer.save()

        from os import remove
        remove(f"{settings.BASE_DIR}\\..\\apps\\users\\api\\docs\\doc.xlsx")
        return Response({"Mensaje": "Se cargo"},status=status.HTTP_201_CREATED)
