from django import forms
from django.forms import ModelForm , fields
from .models import Solicitud 



class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = ['idSolicitud','nombreSolicitud','detalles','imagen','vehiculo','marca']


