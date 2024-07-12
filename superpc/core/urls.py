from django.urls import path
from .views import home, ingresar, nosotros, registrarse, registrarse, ficha_tecnica, solicitud_mantenedor, solicitudes , administacion

urlpatterns = [
    path('',home,name="home"),
    path('ingresar',ingresar, name="ingresar"),
    path('nosotros',nosotros, name="nosotros"),
    path('registrarse',registrarse, name="registrarse"),
    path('ficha_tecnica/<idSolicitud>',ficha_tecnica, name="ficha_tecnica"),
    path('solicitud_mantenedor/<action>/<idSolicitud>',solicitud_mantenedor, name="solicitud_mantenedor"),
    path('solicitudes', solicitudes,name="solicitudes"),
    path('administracion', administacion, name="administracion"),
]
