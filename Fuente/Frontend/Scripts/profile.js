const imagenUsuario = document.getElementById("user-img");

const detectarImagen = ()=>{
    if(imagenUsuario.src == ""){
        imagenUsuario.src = "../../Imagenes/GenericUserProfile.png";
    }
};

detectarImagen();

// Simulación de datos de usuario (reemplaza esto con tu lógica real)
const usuario = {
    nombre: "Juan",
    apellido: "Pérez",
    numero: "123456789",
    imagen: "https://via.placeholder.com/120",
    mail: "juan.perez@email.com",
    password: "********"
};

window.onload = function() {
    document.getElementById('user-nombre').textContent = usuario.nombre;
    document.getElementById('user-apellido').textContent = usuario.apellido;
    document.getElementById('user-numero').textContent = usuario.numero;
    document.getElementById('user-img').src = usuario.imagen;
    document.getElementById('user-mail').textContent = usuario.mail;
    document.getElementById('user-pass').value = usuario.password;

    document.getElementById('change-pass-btn').onclick = function() {
        window.location.href = "cambiar_contraseña.html"; // O muestra un modal
    };

    document.getElementById('back-btn').onclick = function() {
        window.location.href = "index.html";
    };
};