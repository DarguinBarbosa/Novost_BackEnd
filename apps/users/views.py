from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework. response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from apps.users.api.serializers import UserToken
from datetime import datetime
from rest_framework.views import APIView


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        print(login_serializer)
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserToken(user)
                if created:
                    return Response(
                        {
                        'token': token.key, 
                        'user': user_serializer.data,
                        'mensaje': 'Inicio de sesion validado' 
                        }, status= status.HTTP_200_OK
                        )
                else:
                     all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                     if all_sessions.exists():
                         for session in all_sessions:
                             session_data = session.get_decoded()
                             if user.id == int(session_data.get('_auth_user_id')):
                                 session.delete()
                     token.delete()
                     token = Token.objects.create(user = user)
                     return Response(
                         {
                         'token': token.key, 
                         'user': user_serializer.data,
                         'mensaje': 'Inicio de sesion validado' 
                         }, status= status.HTTP_200_OK
                         )
            else:
                return Response({'error': 'El usuario no esta activo'}, status=status.HTTP_401_UNAUTHORIZED)
        else: 
            return Response({'error': 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje': 'Ya hay token'}, status=status.HTTP_200_OK)

class LogOut(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            if token:

                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())

                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()

                session_message = 'Sesiones de usuario cerradas'
                token_message = 'Token eliminado'

                return Response({'token_message': token_message, 'session_message': session_message}, status=status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado un usuario con estas credenciales'})
        except:
            return Response({'error': 'No se ha encontrado un token'}, status=status.HTTP_409_CONFLICT)


        
    