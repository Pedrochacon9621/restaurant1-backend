import django_filters
from .models import Productos

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Productos
        fields = {
            # Habilitar solo 'exact' para 'categoria_prod' y 'nombre_prod'. Este es el por defecto, el que es "igual que"
            'categoria_prod': ['exact'], 
            'nombre_prod': ['exact'],
            
            # 💡 ¡La clave! Habilitar todos los lookups de rango para 'precio_prod'
            'precio_prod': ['exact', 'lte', 'gte', 'lt', 'gt'], 
        }