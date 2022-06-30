$.validator.setDefaults( {
    submitHandler: function () {
       alert( "submitted!" );
    }
 });
 

 $(document).ready(function(){
    $('#signupForm').validate({
       rules: {
          name: {
             required: true,
             minlength: 5
          },
          
          password: {
             required: true,
             minlength: 8
          },
          password2: {
             required: true,
             minlength: 8,
             equalTo: "#password"
          },
          email: {
             required: true,
             email: true
          },
       },
       messages: {           
          name: {
             required: "Por favor ingresa un nombre",
             minlength: "Tu nombre debe ser de no menos de 3 caracteres"
          },
          password: {
             required: "Por favor ingresa una contraseña",
             minlength: "Tu contraseña debe ser de no menos de 8 caracteres"
          },
          password2: {
             required: "Ingresa un password",
             minlength: "Tu contraseña debe ser de no menos de 8 caracteres",
             equalTo: "Por favor ingresa la misma contraseña de arriba"
          },
          email: "Por favor ingresa un correo válido",
       },
       errorElement: "em",
       errorPlacement: function (error, element) {
          error.addClass("help-block");
          if (element.prop( "type" ) === "checkbox") {
             error.insertAfter(element.parent("label") );
          } else {
             error.insertAfter(element);
          }
       },
       highlight: function ( element, errorClass, validClass ) {
          $( element ).parents( ".col-sm-10" ).addClass( "has-error" ).removeClass( "has-success" );
       },
       unhighlight: function (element, errorClass, validClass) {
          $( element ).parents( ".col-sm-10" ).addClass( "has-success" ).removeClass( "has-error" );  
       } 
    });
 });

