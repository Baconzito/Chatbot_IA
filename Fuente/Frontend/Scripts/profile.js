const imagenUsuario = document.getElementById("user-img");

const detectarImagen = ()=>{
    if (!imagenUsuario.getAttribute("src")) {
        imagenUsuario.src = "../Imagenes/GenericUserProfile.png";
    }
};

document.addEventListener("DOMContentLoaded", () => {
    detectarImagen();
});

// Simulación de datos de usuario (reemplaza esto con tu lógica real)
const usuario = {
    nombre: "Juan",
    apellido: "Pérez",
    numero: "123456789",
    mail: "juan.perez@email.com",
    password: "********"
};

window.onload = function() {
    document.querySelector('.user-nombre').textContent = usuario.nombre;
    document.querySelector('.user-apellido').textContent = usuario.apellido;
    document.querySelector('.user-numero').textContent = usuario.numero;
    document.getElementById('user-img').src = usuario.imagen;
    document.querySelector('.user-mail').textContent = usuario.mail;
    document.getElementById('user-pass').value = usuario.password;

    const imagenUsuario = document.getElementById('user-img');
    if (usuario.imagen && usuario.imagen.startsWith('http')) {
        imagenUsuario.src = usuario.imagen;
    } else {
        imagenUsuario.src = "../Imagenes/GenericUserProfile.png";
    }

    
    document.querySelector('.change-pass-btn').onclick = function() {
        window.location.href = "cambiar_contraseña.html"; // O muestra un modal
    };

    document.querySelector('.back-btn').onclick = function() {
        window.location.href = "index.html";
    };
};


const input_IMG = document.querySelector(".input-IMG");
const input_foto = document.querySelector(".input-foto");

input_IMG.addEventListener("click",()=>{
    input_foto.click();
});

input_foto.addEventListener('change', (e)=>{
    const file = e.target.files[0];
    if(file){
        imagenUsuario.src = URL.createObjectURL(file);
    }
});