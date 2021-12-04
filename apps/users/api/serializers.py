from rest_framework import serializers
from apps.users.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class updateFichaApe(serializers.ModelSerializer):
    class Meta:
        model=Aprendiz
        fields =('id','fichaAprendiz')

class UserToken(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nombresUsuario','apellidosUsuario', 'email','rolUsuario','numeroDocumentoUsuario')

class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        fields = '__all__'

    def create(self, validated_data):
        aprendiz = Aprendiz(**validated_data)
        aprendiz.set_password(validated_data['password'])
        aprendiz.save()
        return aprendiz
    
    def update(self, instance, validated_data):
        updated_aprendiz = super().update(instance, validated_data)
        updated_aprendiz.set_password(validated_data['password'])
        updated_aprendiz.save()
        return updated_aprendiz

class AprendizContraCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nombresUsuario' ,'email','password')
    
    def update(self, instance, validated_data):
        updated_aprendiz = super().update(instance, validated_data)
        updated_aprendiz.set_password(validated_data['password'])
        updated_aprendiz.save()
        return updated_aprendiz

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'

class CoordinacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinacion
        fields = '__all__'

class CentroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centro
        fields = '__all__'

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'

    def create(self, validated_data):
        coordinador = Coordinador(**validated_data)
        coordinador.set_password(validated_data['password'])
        coordinador.save()
        return coordinador
    
    def update(self, instance, validated_data):
        updated_coordinador = super().update(instance, validated_data)
        updated_coordinador.set_password(validated_data['password'])
        updated_coordinador.save()
        return updated_coordinador

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

    def create(self, validated_data):
        instructor = Instructor(**validated_data)
        instructor.set_password(validated_data['password'])
        instructor.save()
        return instructor
    
    def update(self, instance, validated_data):
        updated_instructor = super().update(instance, validated_data)
        updated_instructor.set_password(validated_data['password'])
        updated_instructor.save()
        return updated_instructor

class ApoyoAdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApoyoAdministrativo
        fields = '__all__'

    def create(self, validated_data):
        apoyoAdministrativo = ApoyoAdministrativo(**validated_data)
        apoyoAdministrativo.set_password(validated_data['password'])
        apoyoAdministrativo.save()
        return apoyoAdministrativo
    
    def update(self, instance, validated_data):
        updated_apoyoAdministrativo = super().update(instance, validated_data)
        updated_apoyoAdministrativo.set_password(validated_data['password'])
        updated_apoyoAdministrativo.save()
        return updated_apoyoAdministrativo

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

    def create(self, validated_data):
        administrador = Administrador(**validated_data)
        administrador.set_password(validated_data['password'])
        administrador.save()
        return administrador
    
    def update(self, instance, validated_data):
        updated_administrador = super().update(instance, validated_data)
        updated_administrador.set_password(validated_data['password'])
        updated_administrador.save()
        return updated_administrador
    