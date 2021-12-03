from import_export import resources
from .models import Aprendiz

class AprendizResource(resources.ModelResource):
    class Meta:
        model = Aprendiz