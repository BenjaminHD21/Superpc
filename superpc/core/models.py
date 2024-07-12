from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name="idMarca")
    nombreMarca= models.CharField(max_length=150, blank=False, null=False, verbose_name="nombreMarca")

    def __str__(self):
        return self.nombreMarca
    
class Vehiculo(models.Model):
    idVehiculo = models.IntegerField(primary_key=True, verbose_name="idVehiculo")
    nombreVehiculo = models.CharField(max_length=150, blank=False, null=False, verbose_name="nombreVehiculo")

    def __str__(self):
        return self.nombreVehiculo
    
class Solicitud(models.Model):
    idSolicitud = models.IntegerField(primary_key=True , verbose_name="idSolicitud") 
    nombreSolicitud= models.CharField(max_length=50, blank=False , null=False ,verbose_name="nombreSolicitud")
    detalles = models.CharField(max_length=300, null=True, blank=True, verbose_name="detallesSolicutud")
    imagen = models.ImageField(upload_to="img/", default="nn.jpg", blank=False, null=False, verbose_name="Imagen")
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombreSolicitud