from django.shortcuts import render,redirect
from .models import Solicitud, Marca , Vehiculo
from .forms import SolicitudForm
# Create your views here.



def home(request):
    return render(request, "core/home.html")
                  
def ingresar(request):
    return render(request, "core/ingresar.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def administacion(request):
     return render(request, "core/administracion.html")

def registrarse(request):
    return render(request, "core/registrarse.html")

def ficha_tecnica(request, idSolicitud):
    solicitud = Solicitud.objects.get(idSolicitud=idSolicitud)
    data = {"Solicitud": solicitud} 
    return render(request,"core/ficha_tecnica.html",data)

def solicitudes(request):
     data = {"list": Solicitud.objects.all().order_by('idSolicitud')}
     return render(request, "core/solicitudes.html", data)

def solicitud_mantenedor(request , action, idSolicitud):
        data = {"mesg:": "", "form": SolicitudForm,"action": action, "idSolicitud": idSolicitud} 

        if action == 'ins':
            if request.method == "POST":
                form = SolicitudForm(request.POST, request.FILES)
                if form.is_valid:
                    try:
                        form.save()
                        data["mesg"] =  "Solicitud agregada"
                    except:
                        data["mesg"] = "Error al agregar solicitud"     
        elif action == 'upd':
             objeto = Solicitud.objects.get(idSolicitud=idSolicitud)
             if request.method == "POST":
                 form = SolicitudForm(data=request.POST, files=request.FILES, instance=objeto)
                 if form.is_valid:
                     form.save()
                     data["mesg"] = "¡Solicitud Actualozada¡"
             data["form"] = SolicitudForm(instance=objeto)

        elif action == 'del':
                try:
                    Solicitud.objects.get(idSolicitud=idSolicitud).delete()
                    data["mesg"]= "Solicitud Eliminada"
                    return redirect(Solicitud, action='ins', idSolicitud='-1')
                except:
                    data["mesg"]= "Solicitud no existe"
            
        data["list"]= Solicitud.objects.all().order_by('idSolicitud')
        return render(request, "core/solicitud_mantenedor.html", data)
                     
                 
                                 
        