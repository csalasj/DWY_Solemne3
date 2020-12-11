$(document).ready(function () {
    $('form[name="formContacto"]')
        .validate({
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).removeClass('is-invalid');
            },
            submitHandler: function () {
                let txtNombre = $('#txtNombre');
                let txtEmail = $('#txtEmail');
                let txtMensaje = $('#txtMensaje');

                axios.post('http://localhost:8000/contactos/',
                    {
                        nombre: txtNombre.val(),
                        mensaje: txtMensaje.val(),
                        receptor: txtEmail.val(),
                        estado: 'Recepcionado'
                    }).then((respuesta) => {
                        $('#formSuccess').show();
                        console.log(respuesta);
                    }).catch((error) => {
                        console.error(error);
                    })
            },
            rules: {
                txtNombre: {
                    required: true
                },
                txtEmail: {
                    required: true,
                    email: true
                },
                txtMensaje: {
                    required: true
                }
            },
            messages: {
                txtNombre: {
                    required: 'Debes llenar este campo.'
                },
                txtEmail: {
                    required: 'Debes ingresar un correo electrónico.',
                    email: 'El campo del correo no tiene un formato válido de correo'
                },
                txtMensaje: {
                    required: 'No puedes dejar el mensaje vacío.'
                },
            }
        })
})