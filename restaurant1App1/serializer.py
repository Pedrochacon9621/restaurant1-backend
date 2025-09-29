from rest_framework import serializers
from .models import Categorias, Productos, Rol, UsuarioPersonalizado

#SERIALIZERS RUTAS DEFAULT REST FRAMEWORK CRUD------------------------------------------

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Productos
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields='__all__'
class UsuarioPersonalizadoSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=UsuarioPersonalizado
        fields= ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'rol',]
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UsuarioPersonalizado(**validated_data)
        user.set_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

#SERIALIZERS RUTAS DEFAULT REST FRAMEWORK CRUD------------------------------------------

class Categorias2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['id_cat', 'nombre_cat']

#SERIALIZERS RUTA RELACION------------------------------------------

class ProductosCatSerializer(serializers.ModelSerializer):
    categoria_prod = Categorias2Serializer() 
    class Meta:
        model =  Productos
        fields = '__all__'
class UsuarioPersonalizadoRolSerializer(serializers.ModelSerializer):
    rol = RolSerializer() 
    class Meta:
        model =  UsuarioPersonalizado
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'rol',]


