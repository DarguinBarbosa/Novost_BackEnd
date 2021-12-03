from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.deletion import CASCADE
from simple_history.models import HistoricalRecords
from datetime import datetime

class UserManager(BaseUserManager):
    def _create_user(self, tipoDocumentoUsuario, numeroDocumentoUsuario, nombresUsuario,apellidosUsuario, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            tipoDocumentoUsuario = tipoDocumentoUsuario,
            numeroDocumentoUsuario = numeroDocumentoUsuario,
            nombresUsuario = nombresUsuario,
            apellidosUsuario = apellidosUsuario,
            email = email,
            password = numeroDocumentoUsuario,
            is_staff = is_staff,          
            is_superuser = is_superuser,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, tipoDocumentoUsuario, numeroDocumentoUsuario, nombresUsuario,apellidosUsuario, email, password=None, **extra_fields):
        return self._create_user(tipoDocumentoUsuario, numeroDocumentoUsuario, nombresUsuario,apellidosUsuario, email, password, False, False, **extra_fields)

    def create_superuser(self, tipoDocumentoUsuario, numeroDocumentoUsuario, nombresUsuario,apellidosUsuario, email, password=None, **extra_fields):
        return self._create_user(tipoDocumentoUsuario, numeroDocumentoUsuario, nombresUsuario,apellidosUsuario, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    TIPO_DOCUMENTO = (
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('NCS', 'Número ciego SENA'),
        ('PS', 'Pasaporte'),
        ('DNI', 'Documento Nacional de Identificación'),
        ('NIT', 'Número de Identificación Tributaria'),
        ('PR', 'PEP - RAMV'),
        ('PEP', 'PEP'),
    )

    ROL_USUARIO = (
        ('IN', 'Instructor'),
        ('AP', 'Aprendiz'),
        ('AA', 'Apoyo administrativo'),
        ('CO', 'Coordinador'),
        ('AD', 'Administrador'),
    )

    tipoDocumentoUsuario = models.CharField(max_length=3, choices=TIPO_DOCUMENTO, blank=True, default='CC')
    numeroDocumentoUsuario = models.IntegerField(unique = True)  
    nombresUsuario = models.CharField(max_length = 255, blank = True, null = True)
    apellidosUsuario = models.CharField(max_length = 255, blank = True, null = True)
    rolUsuario = models.CharField(max_length=2, choices=ROL_USUARIO, blank=False)
    email = models.EmailField(max_length = 255, unique = True)
    image = models.ImageField(upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    history = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'numeroDocumentoUsuario'
    REQUIRED_FIELDS = ['tipoDocumentoUsuario','nombresUsuario','apellidosUsuario', 'email']

    def __str__(self):
        return f'{self.nombresUsuario} {self.apellidosUsuario}'

class Ficha(models.Model):
    anios = []
    for r in range(2018, (datetime.now().year+1)):
        anios.append((r,r))
# Cambie la ficha
    nombreCentro = models.CharField(max_length=255,  blank = True, null = True)
    nombreCoordinacion = models.CharField(max_length=255,  blank = True, null = True)
    nombrePrograma = models.CharField(max_length=255,  blank = True, null = True)
    versionPrograma = models.CharField(max_length=255, blank = True, null = True)
    idFicha = models.AutoField(primary_key = True)
    numeroFicha = models.IntegerField(unique = True)
    anio = models.IntegerField(verbose_name = "Año", choices = anios ,default=datetime.now().year)
    trimestre = models.IntegerField()
    cantidadAprendices = models.IntegerField()
    
    class Meta:
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"

    def __str__(self):
        return str(self.numeroFicha)

class Aprendiz(User):
    telefonoAprendiz = models.BigIntegerField() 
    estadoAprendiz = models.CharField(max_length=200, blank= False, null= False)
    fichaAprendiz = models.ForeignKey(Ficha, on_delete=CASCADE)

    class Meta:
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"

    def __str__(self):
        return "Apr. %s %s"%(self.nombresUsuario,self.apellidosUsuario)


class Coordinacion(models.Model):
    idCoordinacion = models.AutoField(primary_key = True)
    nombreCoordinacion = models.CharField(max_length=200, blank= False, null= False)
    
    class Meta:
        verbose_name = "Coordinacion"
        verbose_name_plural = "Coordinaciones"

    def __str__(self):
        return self.nombreCoordinacion


class Centro(models.Model):
    idCentro = models.AutoField(primary_key = True)
    nombreCentro = models.CharField(max_length=200, blank= False, null= False)
    
    class Meta:
        verbose_name = "Centro"
        verbose_name_plural = "Centros"

    def __str__(self):
        return self.nombreCentro

class Coordinador(User):
    coordinacion = models.ForeignKey(Coordinacion, on_delete=CASCADE)
    centro = models.ForeignKey(Centro, on_delete=CASCADE)

    class Meta:
        verbose_name = "Coordinador"
        verbose_name_plural = "Coordinadores"

    def __str__(self):
        return "Coordinador. %s %s"%(self.nombresUsuario,self.apellidosUsuario)

class Asignatura(models.Model):
    idAsignatura = models.AutoField(primary_key = True)
    nombreAsignatura = models.CharField(max_length=200, blank= False, null= False)
    
    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self):
        return self.nombreAsignatura

class Instructor(User):

    ROL_INSTRUCTOR = (
        ('LF', 'Instructor lider de ficha'),
        ('LP', 'Instructor lider apoyo administrativo'),
        ('LA', 'Instructor lider de asignatura'),
    )

    rolInstructor = models.CharField(max_length=2, choices=ROL_INSTRUCTOR, blank=False, default='LA')
    jefeInmediato = models.ForeignKey(Coordinador, on_delete=CASCADE)
    coordinacion = models.ForeignKey(Coordinacion, on_delete=CASCADE)
    numeroFichaLider = models.ForeignKey(Ficha, on_delete=CASCADE, blank=True, null=True)
    asignatura = models.ForeignKey(Asignatura, on_delete=CASCADE,  blank=True, null=True)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    def __str__(self):
        return "Ins. %s %s"%(self.nombresUsuario,self.apellidosUsuario)

class ApoyoAdministrativo(User):
    coordinacion = models.ForeignKey(Coordinacion, on_delete=CASCADE)

    class Meta:
        verbose_name = "Apoyo admnistrativo"
        verbose_name_plural = "Apoyos administrativos"

    def __str__(self):
        return "Apoyo admin. %s %s"%(self.nombresUsuario,self.apellidosUsuario)

class Administrador(User):
    correoAlterno = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return "Admin. %s %s"%(self.nombresUsuario,self.apellidosUsuario)