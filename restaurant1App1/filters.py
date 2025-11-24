import django_filters
from .models import Productos, Categorias, UsuarioPersonalizado
from django.db.models import Q


class ProductoFilter(django_filters.FilterSet):
    # Funcion para barra de busqueda - Buscar por nombre o categoria.
    busqueda = django_filters.CharFilter(method='buscar_por_nombre_o_categoria')
    def buscar_por_nombre_o_categoria(self, queryset, name, value):
        return queryset.filter(
            Q(nombre_prod__icontains=value) |
            Q(categoria_prod__nombre_cat__icontains=value)
        )

    class Meta:
        model = Productos
        fields = {
            # Habilitar solo 'exact' para 'categoria_prod' y 'nombre_prod'. Este es el por defecto, el que es "igual que"
            'categoria_prod': ['exact'], 
            'nombre_prod': ['exact', 'icontains'],
            
            # 💡 ¡La clave! Habilitar todos los lookups de rango para 'precio_prod'
            'precio_prod': ['exact', 'lte', 'gte', 'lt', 'gt'], 
        }

class CategoriaFilter(django_filters.FilterSet):
    class Meta:
        model = Categorias
        fields = {
            'nombre_cat' : ['exact', 'icontains'],
        }

class UsuarioFilter(django_filters.FilterSet):
    busqueda = busqueda = django_filters.CharFilter(method='buscar_user')
    def buscar_user(self, queryset, name, value):
        return queryset.filter(
            Q(username__icontains=value) |
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
        )
    class Meta:
        model = UsuarioPersonalizado
        fields = {
            'username' : ['exact'],
            'first_name' : ['exact'],
            'last_name' : ['exact'],
        }