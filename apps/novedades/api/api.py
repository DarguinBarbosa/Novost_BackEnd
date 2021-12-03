from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from apps.novedades.models import DetalleNovedad,Novedad,TipoNovedad
from apps.novedades.api.serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST','PUT'])
def insertar(request):
    if request.method=='POST':
        insertar = insertarNove(data=request.data)
        print(request.data)
        if insertar.is_valid(True):
            print(request.data)
            insertar.save()
            return Response(insertar.data,  status=status.HTTP_201_CREATED)
        else:
            return Response(insertar.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        print(request)
        noveid=DetalleNovedad.objects.get(id=request.data['id'])
        print(request.data)
        detalleSeria=DetalleNovedadSerializer(noveid, data=request.data)
        if detalleSeria.is_valid(True):
            detalleSeria.save()
            return JsonResponse(detalleSeria.data,status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)

    



@api_view(['GET', 'PUT'])
def getId(request, pk):
    try: 
        detalleid=DetalleNovedad.objects.filter(id=pk)
        print(detalleid)
        detalleSeria=DetalleNovedadSerializer(detalleid, many=True)
        return JsonResponse(detalleSeria.data, safe=False)
    except DetalleNovedad.DoesNotExist: 
        return JsonResponse({'message': 'No se encontraron registro'}, status=status.HTTP_404_NOT_FOUND) 

"""
@api_view(['PUT', 'POST'])
def Createnove(request):
    if request.method=='POST':
        print(request.data)
        serializers=NovedadSerlizers(data=request.data)
        print(serializers)
        if serializers.is_valid():
                print(serializers.save())
                serializers.save()
                return JsonResponse(serializers.data,status=status.HTTP_201_CREATED) 
        return JsonResponse(serializers.errors)
    print(request)
    if request.method=='PUT':
        #print(request.data)
        noveid=Novedad.objects.get(id=request.data['id'])
        detalleSeria=NovedadSerlizers2(noveid, data=request.data)
        if detalleSeria.is_valid(True):
            detalleSeria.save()
            return JsonResponse(detalleSeria.data,status=status.HTTP_201_CREATED)
        return JsonResponse(detalleSeria.errors,status=status.HTTP_201_CREATED)
"""

@csrf_exempt
def detalleApi(request,id=0):
    if request.method=='GET':
        detalle = DetalleNovedad.objects.all()
        detalleSeria=DetalleNovedadSerializer(detalle, many=True)
        return JsonResponse(detalleSeria.data, safe=False)
    elif request.method=='POST':
        detalleData=JSONParser().parse(request)
        detalleSeria=DetalleNovedaderializer(data=detalleData)
        print(detalleSeria)
        if detalleSeria.is_valid(True):
            print(detalleSeria)
            detalleSeria.save()
            return JsonResponse('Agregado',safe=False)
        return JsonResponse('Documento NO agregado',safe=False)
    elif request.method=='PUT':
        detalleData=JSONParser().parse(request)
        detalleid=DetalleNovedad.objects.get(id=detalleData['id'])
        detalleSeria=UpdateDetalle(detalleid,data=detalleData)
        print(detalleSeria)
        if detalleSeria.is_valid():
            detalleSeria.save()
            return JsonResponse('Actualizado',safe=False)
        return JsonResponse('Error al Actulizar',safe=False)
    elif request.method=='DELETE':
        detalleid=DetalleNovedad.objects.get(id=id)
        detalleid.delete()
        return JsonResponse('USUARIO ELIMINADO',safe=False)
    return JsonResponse('El docuemnto No ha sido  ELIMINADO',safe=False)



@api_view(['GET', 'PUT', 'DELETE'])
def getnove(request, pk):

    try: 
        idvalue=DetalleNovedad.objects.filter(id=pk)
        datos=NovedadSerlizers(idvalue, many=True)
        return JsonResponse(datos.data, safe=False)
    except Novedad.DoesNotExist: 
        return JsonResponse({'message': 'No se encontraron registro'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def AprendizNovedad(request, pk):
    try: 
        idvalue=DetalleNovedad.objects.filter(aprendizNovedad=pk)
        datos=NovedadSerlizers(idvalue, many=True)
        return JsonResponse(datos.data, safe=False)
    except Novedad.DoesNotExist: 
        return JsonResponse({'message': 'No se encontraron registro'}, status=status.HTTP_404_NOT_FOUND) 




@csrf_exempt
def NovedadApi(request,id=0):
    if request.method=='GET':
        novedad = Novedad.objects.all()
        noveSeria=NovedadSerlizers(novedad, many=True)
        return JsonResponse(noveSeria.data, safe=False)
    elif request.method=='POST':
        noveData=JSONParser().parse(request)
        print(noveData)
        noveSeria=NovedadSerlizers(data=noveData)
        if noveSeria.is_valid(True):
            print(noveSeria)
            noveSeria.save()
            return JsonResponse('Agregado',safe=False)
        return JsonResponse('Documento NO agregado',safe=False)
    elif request.method=='PUT':
        print(request)
        noveid=Novedad.objects.get(id=request.data['id'])
        detalleSeria=NovedadSerlizers(noveid,data=novedad_data)
        print('-----------------------------'+detalleSeria)
        if detalleSeria.is_valid(True):
            #detalleSeria.save()
            return JsonResponse('Actualizado',safe=False)
        return JsonResponse('Error al Actulizar',safe=False)
    elif request.method=='DELETE':
        noveid=Novedad.objects.get(id=id)
        noveid.delete()
        return JsonResponse('USUARIO ELIMINADO',safe=False)
    return JsonResponse('El docuemnto No ha sido  ELIMINADO',safe=False)




@api_view(['GET', 'PUT', 'DELETE'])
def getId1(request, pk):
    # find tutorial by pk (id)
    try: 
        idvalue=TipoNovedad.objects.filter(id=pk)
        datos=tipoNovedadSerlizers(idvalue, many=True)
        return JsonResponse(datos.data, safe=False)
    except DetalleNovedad.DoesNotExist: 
        return JsonResponse({'message': 'No se encontraron registro'}, status=status.HTTP_404_NOT_FOUND) 

@csrf_exempt
def tipoNovedadApi(request,id=0):
    if request.method=='GET':
        tiponovedad = TipoNovedad.objects.all()
        noveSeria=tipoNovedadSerlizers(tiponovedad, many=True)
        print(noveSeria.data)
        return JsonResponse(noveSeria.data, safe=False)
    elif request.method=='POST':
        noveData=JSONParser().parse(request)
        noveSeria=tipoNovedadSerlizers(data=noveData)
        print(noveSeria.is_valid())
        if noveSeria.is_valid():
            print(noveSeria)
            noveSeria.save()
            return JsonResponse('Agregado',safe=False)
        return JsonResponse('Documento NO agregado',safe=False)
    elif request.method=='PUT':
        novedad_data=JSONParser().parse(request)
        noveid=TipoNovedad.objects.get(id=novedad_data['id'])
        detalleSeria=tipoNovedadSerlizers(noveid,data=novedad_data)
        if detalleSeria.is_valid(True):
            detalleSeria.save()
            return JsonResponse('Actualizado',safe=False)
        return JsonResponse('Error al Actulizar',safe=False)
    elif request.method=='DELETE':
        noveid=TipoNovedad.objects.get(id=id)
        noveid.delete()
        return JsonResponse('USUARIO ELIMINADO',safe=False)
    return JsonResponse('El docuemnto No ha sido  ELIMINADO',safe=False)
        

@api_view(['GET', 'POST'])
def post(request):
    print(request.data)
    serializers=NovedadSerlizers(data=request.data)
    print(serializers)
    return HttpResponse({'message': 'Book created'}, status=200)




@api_view(['PUT'])
def UpdateEstadoNo(request):
    if request.method=='PUT':
        #print(request.data)
        noveid=Novedad.objects.get(id=request.data['id'])
        detalleSeria=solicitudUpdate(noveid, data=request.data)
        if detalleSeria.is_valid(True):  
            detalleSeria.save()
            return JsonResponse(detalleSeria.data,status=status.HTTP_201_CREATED)
        return JsonResponse(detalleSeria.errors,status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def solicitud(request):
    if request.method=='PUT':
        print(request.data)
        noveid=Novedad.objects.get(id=request.data['id'])
        detalleSeria=solicitudD(noveid, data=request.data)
        print(detalleSeria)
        if detalleSeria.is_valid(True):  
            detalleSeria.save()
            return JsonResponse(detalleSeria.data,status=status.HTTP_201_CREATED)
        return JsonResponse(detalleSeria.errors,status=status.HTTP_201_CREATED)
