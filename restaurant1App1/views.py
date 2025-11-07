from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ProductosSerializer, CategoriasSerializer, ProductosCatSerializer, UsuarioPersonalizadoSerializer, RolSerializer, UsuarioPersonalizadoRolSerializer
from .models import Productos, Categorias, UsuarioPersonalizado, Rol
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdmin
from .filters import ProductoFilter



# Create your views here.

class CategoriasView(viewsets.ModelViewSet):
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()] #todos pueden consultar
        elif self.action == 'destroy':  # DELETE
            return [IsAuthenticated(), IsAdmin()]#solo los admin pueden eliminar
        return [IsAuthenticated()]#para actualizar o agregar debes autenticar

class ProductosView(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()
    filterset_class = ProductoFilter
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()] #todos pueden consultar
        elif self.action == 'destroy':  # DELETE
            return [IsAuthenticated(), IsAdmin()]#solo los admin pueden eliminar
        return [IsAuthenticated()]#para actualizar o agregar debes autenticar

class RolView(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

class UsuarioPersonalizadoView(viewsets.ModelViewSet):
    serializer_class = UsuarioPersonalizadoSerializer
    queryset = UsuarioPersonalizado.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

class ProductosCatView(viewsets.ModelViewSet):
    serializer_class = ProductosCatSerializer
    queryset = Productos.objects.all()
    filterset_class = ProductoFilter
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()] #todos pueden consultar
        elif self.action == 'destroy':  # DELETE
            return [IsAuthenticated(), IsAdmin()]#solo los admin pueden eliminar
        return [IsAuthenticated()]#para actualizar o agregar debes autenticar
    
class UsuarioPersonalizadoRolView(viewsets.ModelViewSet):
    serializer_class = UsuarioPersonalizadoRolSerializer
    queryset = UsuarioPersonalizado.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

#Clase para verificar datos del usuario logeado:
class MeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UsuarioPersonalizadoSerializer(request.user)
        return Response(serializer.data)

