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
    imagen: "https://via.placeholder.com/120",
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

    document.querySelector('.change-pass-btn').onclick = function() {
        window.location.href = "cambiar_contraseña.html"; // O muestra un modal
    };

    document.querySelector('.back-btn').onclick = function() {
        window.location.href = "index.html";
    };
};

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

const token = getCookie('token');
if (token) {
    // Decodificá el payload (solo lectura, sin verificar)
    const payload = JSON.parse(atob(token.split('.')[1]));
    console.log("Usuario logueado:", payload.email);
} else {
    window.location.href = 'login.html';
}

token();