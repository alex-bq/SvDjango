

$(document).ready(function () {
    $("#formulario_contacto").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3,
                maxlength: 30
            },
            email: {
                required: true,
                email: true

            },
            tipo_documento: {
                required: true
            },
            rut: {
                required: true,
                minlength: 11,
                maxlength: 12,
                
            },
            telefono: {
                required: false,
                minlength: 8,
                maxlength: 9
            },
            ciudad: {
                required: true
            },
            mensaje: {
                required: true,
                minlength: 50
            }
        },
        messages: {
            nombre: {
                required: " Por favor ingresa tu nombre",
                minlength: " Tu nombre debe ser de no menos de 3 caracteres"
            },
            email: {
                required: "Por favor ingresa un corrreo",
                email: "Por favor ingresa un correo válido"
            },
            tipo_documento: {
                required: "Por favor selecciona un tipo de documento"

            },
            rut: {
                required: "Por favor ingresa un rut valido",
                minlength: "Por favor ingresa un rut valido",
                maxlength: "Por favor ingresa un rut valido",
                

            },
            telefono: {
                minlength: "Por favor Ingresa un numero valido",
                maxlength: "Por favor Ingresa un numero valido"
            },
            ciudad: {
                required: "Por favor Selecciona una ciudad"
            },
            mensaje: {
                required: "Por favor ingresa un comentario",
                minlength: "El mensaje debe ser de al menos 50 caracteres"
            }
        }

    })
})








