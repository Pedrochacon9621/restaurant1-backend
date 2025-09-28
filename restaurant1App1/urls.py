from django.urls import path, include
from rest_framework import routers
from .views import CategoriasView, ProductosView, ProductosCatView, UsuarioPersonalizadoView, RolView, UsuarioPersonalizadoRolView, MeView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

router = routers.DefaultRouter() #Crear varibale para definir las rutas del CRUD por DEFECTO que trae Rest Framework

#Utilizacion de variable router para las rutas por defecto de REST FRAMEWORK:
router.register(r'categorias', CategoriasView, 'categoria')
router.register(r'productos', ProductosView, 'productos')
router.register(r'productosc', ProductosCatView, 'productosc')
router.register(r'usuarios', UsuarioPersonalizadoView, 'usuarios')
router.register(r'usuariosr', UsuarioPersonalizadoRolView, 'usuariosr')
router.register(r'rol', RolView, 'rol') 

urlpatterns = [
    path('', include(router.urls)), #Rutas por defecto De REST FRAMEWORK
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
]