function ocultarDescripcion(card) {
    var desc = card.querySelector('.descripcion');
    desc.style.display = 'none';
  }

  function mostrarDescripcion(card) {
    var desc = card.querySelector('.descripcion');
    desc.style.display = 'block';
  }

  $(document).ready(function() {
    $('#comuna').click(function() {
        $.get('https://api.shipit.cl/v/regions', function(data) {
            $('#comuna').empty();
               $.each(data, function (i, item)  {
                var option = '<option>' + item.name + ' ' + item.roman_numeral + '</option>';
                $('#comuna').append(option);
            });
        });
    });
});

function limpiar() {

    document.getElementById('RUT').value = "";
    document.getElementById('nombre').value = "";
    document.getElementById('apellido').value = "";
    document.getElementById('email').value = "";
    document.getElementById('imagen').value = "";
    document.getElementById('si').checked = false;
    document.getElementById('no').checked = false;
    document.getElementById('marca').value = "";
    document.getElementById('contraseña1').value = "";
    document.getElementById('contraseña2').value = "";
}





$(document).ready(function() {
    $("#formulario").validate({
        rules: {
            rut:{
                required: true,
            },
            nombre:{
                required: true,
            },
            apellido:{
                required: true,
            },
            correo:{
                required: true,
            },
            contraseña1:{
                required: true,
            },
            contraseña2:{
                required: true,
                equalTo: "#contraseña1",
            },
            sexo:{
                required: true,
            },
            imagen:{
                required: true,
            },
            vehiculo:{
                required: true,
            },
            marca:{
                required: true,
            }
        },
        messages:{
            rut:{
                required: "por favor ingresar un rut",
            },
            nombre:{
                required: "por favor ingresar un nombre",
            },
            apellido:{
                required: "por favor ingresar un apellido",
            },
            correo:{
                required: "por favor ingresar un correo",
            },
            contraseña1:{
                required: "por favor ingresar contraseña",
            },
            contraseña2:{
                required: "por favor ingresar contraseña",
                equalTo: "las contraseña no coinciden",
            },
            sexo: {
                required: "por favor seleccionar sexo",
            },
            imagen: {
                required: "por favor ingresar imagen",
            },
            vehiculo: {
                required: "por favor seleccionar vehiculo",
            },
            marcas: {
                required: "por favor ingresar marca del vehiculo",
            },

        },
    });
});





    $(document).ready(function () {

        $.get('https://api.shipit.cl/v/regions', function (data) {
      
          $.each(data, function (i, item) {
      
            var card = '';
            card += '<div class="col-lg-3 col-md-4 col-sm-6 mb-4">';
            card += '  <div class="card h-100">';
            card += '    <div class="card-body">';
            card += '      <h5 class="card-title truncate">' + item.name + '</h5>';
            card += '      <p class="card-text">';
            card += '        <span class="stock">' + item.number+ '</span>';
            card += '      </p>';
            card += ' <p class="card-text">'+item.roman_numeral+'</p>';
            card += '<p class="card-text">'+item.country_id+ '</p>';
            card += '    </div>';
            card += '  </div>';
            card += '</div>';
      
            $('#contenedor-comunas').append(card);
      
          });
      
        });
    });


// Espera a que el documento HTML esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Obtén todos los elementos de la clase "card-text"
    var descripciones = document.getElementsByClassName('card-text');
  
    // Itera sobre cada elemento de descripción
    for (var i = 0; i < descripciones.length; i++) {
      var descripcion = descripciones[i];
      var botonMostrar = document.createElement('button');
      botonMostrar.textContent = 'Mostrar descripción';
      botonMostrar.classList.add('btn');
      botonMostrar.classList.add('btn-sm');
      botonMostrar.classList.add('btn-primary');
      botonMostrar.addEventListener('click', function() {
        var descripcion = this.parentNode.querySelector('.card-text');
        if (descripcion.style.display === 'none') {
          descripcion.style.display = 'block';
          this.textContent = 'Ocultar descripción';
        } else {
          descripcion.style.display = 'none';
          this.textContent = 'Mostrar descripción';
        }
      });
  
      // Inserta el botón antes de la descripción
      descripcion.parentNode.insertBefore(botonMostrar, descripcion);
      descripcion.style.display = 'none';
    }
  });