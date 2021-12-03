from django.contrib import admin
from apps.users.models import *

class AprendizAdmin(admin.ModelAdmin):
     exclude = ('is_superuser','is_staff','extra_fields','last_login','groups','user_permissions','image','is_active','password')

class InstructorAdmin(admin.ModelAdmin):
     exclude = ('is_superuser','is_staff','extra_fields','last_login','groups','user_permissions','image','is_active','password')

class CoordinadorAdmin(admin.ModelAdmin):
     exclude = ('is_superuser','is_staff','extra_fields','last_login','groups','user_permissions','image','is_active','password')

class ApoyoAdministrativoAdmin(admin.ModelAdmin):
     exclude = ('is_superuser','is_staff','extra_fields','last_login','groups','user_permissions','image','is_active','password')

class AdministradorAdmin(admin.ModelAdmin):
     exclude = ('is_superuser','is_staff','extra_fields','last_login','groups','user_permissions','image','is_active','password')

admin.site.register(User)
admin.site.register(Aprendiz, AprendizAdmin)
admin.site.register(Ficha)
admin.site.register(Coordinacion)
admin.site.register(Centro)
admin.site.register(Asignatura)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Coordinador, CoordinadorAdmin)
admin.site.register(ApoyoAdministrativo, ApoyoAdministrativoAdmin)
admin.site.register(Administrador, AdministradorAdmin)