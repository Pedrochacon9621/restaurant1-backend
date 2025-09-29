from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Categorias(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nombre_cat = models.CharField(max_length=50)
    descripcion_cat = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_cat

class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=100)
    #img_prod = models.ImageField(upload_to='productos/', blank=True, null=True)
    img_prod = CloudinaryField('image', folder='restaurant1App1/productos', blank=True, null=True)
    descripcion_prod = models.TextField()
    precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    categoria_prod = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, related_name='productos') # no se elimina el producto, y related_name para hacer consulta con relacion ORM.
    disponible = models.BooleanField(default=True)
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos", null=True, blank=True)
    destacado = models.BooleanField(default=False)
    fecha_creacion_prod = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_prod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_prod
    

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class UsuarioPersonalizado(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

    