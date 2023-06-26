//Crear una constante llamada formulario
const formulario = document.getElementById('formulario_feliz');
//Arreglo con todos los inputs del formulario
const inputs = document.querySelectorAll('#formulario_feliz input');
//EXPRESIONES PARA LAS VÁLIDACIONES
const expresiones = {
    usuario:/^[a-zA-Z0-9\_\-]{4,16}$/,
    password: /^[a-z0-9]{6,14}$/,
    nombre:/^[a-zA-Z]{3,10}$/,
    apellido:/^[a-zA-Z]{3,10}$/,
    correo:/^[a-z0-9_.+-]+@+[a-z]+\.[a-z]+$/,
    run:/^[0-9]+-[0-9kK]{1}$/,
}

const validarFormulario = (e)=>{
    switch(e.target.name){
        case"nombre":
        if(expresiones.nombre.test(e.target.value)){
            
        }else{
            alert("No se aceptan símbolos o números para el nombre")
        }
        break;
        case"apellido":
        if(expresiones.apellido.test(e.target.value)){
           
        }else{
            alert("No ingrese símbolos o números en el apellido")
        }
        break;
        case"run":
        if(expresiones.run.test(e.target.value)){
            
        }else{
            alert("Ingrese su rut con guion y dígito verificador. SIN PUNTOS")
        }
           
        break;
        case"correo":
        if(expresiones.correo.test(e.target.value)){
           
        }else{
            alert("Email inválido")
        }
        break;
        case"usuario":
            if(expresiones.usuario.test(e.target.value)){
           
            }else{
               alert("El usuario debe contener por lo menos 4 caracteres")
            }
        break;
        case"password":
            if(expresiones.password.test(e.target.value)){
            
            }else{
                alert("La contraseña debe tener entre 6 a 14 caracteres y puede ser alfanumerica")
            
            }
        break;
        case"check":
            console.log('fsnd')
        break;
    }

}
inputs.forEach((input)=>{
   // input.addEventListener('keyup',validarFormulario); //soltar tecla
    input.addEventListener('blur',validarFormulario); //presionar fuera del input
    // console.log('Tecla levantada'); para ver si funciona
}
);
//Ejecutar función al hacer click en el botón de tipo submit
//e va a ser un parametro que sera un evento
formulario.addEventListener('submit',(e)=>{
    //preventDefaul es para que la página no envie o no haga nada
    e.preventDefault();
    
});



//documento cargado
$(document).ready(
    
   function(){
       $("#emailInput").focus(function(){
          console.log("foco en el campo realizado");
        })
    } 
    );
